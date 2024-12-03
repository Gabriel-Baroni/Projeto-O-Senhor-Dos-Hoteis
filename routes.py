#Importa do framework Flask algumas funcionalidades
from flask import render_template, request, redirect, url_for, session, flash
#Importa o conversor de strings em objetos de data
from datetime import datetime
import smtplib
from email.message import Message
 
#Faz a função principal das rotas e recebe os parâmetros: do objeto do flask e do BDD 
def init_routes(app, supabase):

    # Rota para a tela inicial (index.html)
    @app.route("/", methods=["GET", "POST"])
    def homepage():
        #Verifica se a reserva já foi expirada: Se sim a joga para tabela das expiradas e remove das reservas
        data_atual = datetime.now().date()
        response=supabase.table("Reserva").select("*").lte("checkout", data_atual).execute()
        for reserva in response.data:
            supabase.table("Reserva_expirada").insert(reserva).execute()
            response=supabase.table("Reserva").delete().eq("id", reserva['id']).execute()
            
        usuario_id = session.get("usuario_id")
        usuario_email = None
        if usuario_id:
            user_response = supabase.table("User").select("email").eq("id", usuario_id).execute()
            if user_response.data:
                usuario_email = user_response.data[0]["email"]
        return render_template("index.html", usuario_email=usuario_email)  
        

    # Rota para a página de resultados dos quartos (quartos.html)
    @app.route("/quartos", methods=["POST"])
    def quartos():
        data_atual = datetime.now().date()
        numero_pessoas = int(request.form.get("numero_pessoas"))
        checkin = request.form.get("checkin")
        checkout = request.form.get("checkout")
        session["checkin"] = checkin
        session["checkout"] = checkout

        #Converte as datas de string para datetime (sem a hora)
        try:
            data_checkin = datetime.strptime(checkin, "%Y-%m-%d").date()
            data_checkout = datetime.strptime(checkout, "%Y-%m-%d").date()
        except ValueError:
            flash("Datas inválidas. Use o formato AAAA-MM-DD.")
            return redirect(url_for("homepage"))

        #Condicionais para as datas de Check-in e Check-out
        if data_checkout <= data_checkin:
            flash("A data de checkout deve ser posterior à data de check-in.")
            return redirect(url_for("homepage"))
        if data_checkin < data_atual or data_checkout<data_atual:
            flash("A data não pode ser menor do que a data atual")
            return redirect(url_for("homepage"))
        
        # Consultando os quartos com capacidade suficiente
        response = supabase.table("Quarto").select("*").gte("capacidade", numero_pessoas).execute()
        quartos_disponiveis = []
        
        # Percorre a consulta ao BDD e verifica pelo ID os quartos disponíveis 
        for quarto in response.data:
            reservas_conflict = supabase.table("Reserva").select("*").eq("quarto_id", quarto["id"]).execute()

            conflito = False 
            
            #Percorre as reservas existentes pelo id
            for reserva in reservas_conflict.data:
                reserva_checkin = datetime.strptime(reserva["checkin"], "%Y-%m-%d").date()
                reserva_checkout = datetime.strptime(reserva["checkout"], "%Y-%m-%d").date()

                #Se tiver confilto entre as datas
                if not (data_checkout <= reserva_checkin or data_checkin >= reserva_checkout):
                    conflito = True
                    break  
            # Se não tiver conflito adiciona o quarto a lista
            if not conflito:
                quartos_disponiveis.append(quarto)

        usuario_id = session.get('usuario_id')
        return render_template("quartos.html", quartos=quartos_disponiveis, usuario_id=usuario_id)

    # Rota para a página de reserva de um quarto específico (reserva.html)
    @app.route("/reserva/<int:quarto_id>", methods=["GET", "POST"])
    def reserva(quarto_id):
        if request.method == "GET":
            # Recupera os detalhes do quarto pelo ID
            response = supabase.table("Quarto").select("*").eq("id", quarto_id).execute()
            if not response.data:
                flash("Quarto não encontrado.")
                return redirect(url_for("homepage"))

            quarto = response.data[0]
            checkin = session.get("checkin")
            checkout = session.get("checkout")
            
            if not checkin or not checkout:
                flash("As datas de check-in e check-out não estão disponíveis. Por favor, reinicie a busca.")
                return redirect(url_for("homepage"))

            # Calcula o total de dias e o preço total
            data_checkin = datetime.strptime(checkin, "%Y-%m-%d")
            data_checkout = datetime.strptime(checkout, "%Y-%m-%d")
            dias = (data_checkout - data_checkin).days
            preco_total = dias * quarto["preco_diaria"]

            return render_template("reserva.html", quarto=quarto, preco_total=preco_total)

        elif request.method == "POST":
            # Confirmar reserva
            usuario_id = session.get("usuario_id")
            if not usuario_id:
                flash("Você precisa estar logado para fazer uma reserva.")
                return redirect(url_for("login_cadastro"))

            checkin = session.get("checkin")
            checkout = session.get("checkout")
            response = supabase.table("Quarto").select("*").eq("id", quarto_id).execute()
            if not response.data:
                flash("Quarto não encontrado.")
                return redirect(url_for("homepage"))

            quarto = response.data[0]

            # Calcula o preço total
            data_atual = datetime.now().date()
            data_checkin = datetime.strptime(checkin, "%Y-%m-%d").date()
            data_checkout = datetime.strptime(checkout, "%Y-%m-%d").date()
            dias = (data_checkout - data_checkin).days
            preco_total = dias * quarto["preco_diaria"]



            # Insere a reserva no banco de dados
            reserva_data = {
                "usuario_id": usuario_id,
                "quarto_id": quarto_id,
                "checkin": checkin,
                "checkout": checkout,
                "preco_total": preco_total,
                "data_reserva": data_atual.isoformat()
            }

            reserva_response = supabase.table("Reserva").insert(reserva_data).execute()
            if not reserva_response.data:
                flash("Erro ao confirmar a reserva.")
                return redirect(url_for("homepage"))

            # Atualiza a disponibilidade do quarto
            supabase.table("Quarto").update({"disponiblidade": 0}).eq("id", quarto_id).execute()
            flash("Reserva confirmada com sucesso!")
            return redirect(url_for("homepage"))

    # Rota para a tela de login e cadastro
    @app.route("/login_cadastro", methods=["GET", "POST"])
    def login_cadastro():
        if request.method == "POST":
            action = request.form.get("action")
            if action == "cadastro":
                nome = request.form.get("nome")
                email = request.form.get("email")
                senha = request.form.get("senha")
                tel = request.form.get("tel")

                data = {
                    "nome": nome,
                    "email": email,
                    "senha": senha,
                    "tel": tel
                }

                response = supabase.table("User").insert(data).execute()
                
                supabase.auth.sign_up({ "email": email, "password": senha})

                if response.data:
                    flash("Cadastro realizado com sucesso!")
                    return redirect(url_for('homepage'))
                else:
                    flash("Erro ao cadastrar usuário.")
                    return redirect(url_for("login_cadastro"))

            elif action == "login":
                email = request.form.get("email")
                senha = request.form.get("senha")
                response = supabase.table("User").select("*").eq("email", email).eq("senha", senha).execute()

                if  response.data:
                    usuario = response.data[0]
                    session['usuario_id'] = usuario['id']
                    flash("Login realizado com sucesso!")
                    return redirect(url_for('homepage'))
                else:
                    flash("Erro no login: usuário não encontrado ou senha incorreta.")
                    return redirect(url_for("login_cadastro"))

        return render_template("login_cadastro.html")
    @app.route("/logout")
    def logout():
        session.pop("usuario_id", None)  # Remove o ID do usuário da sessão
        flash("Você saiu da conta com sucesso.", "info")
        return redirect(url_for("homepage"))


    # Rota para a tela de informações do hotel
    @app.route("/about")
    def about():
        return render_template("about.html")

    # Rota para a tela de suporte
    @app.route("/suport", methods=["POST", "GET"])
    def suport():
        if request.method == "POST":
            email_usuario = request.form.get("email")
            corpo_email= request.form.get("assunto")
            senha = ""  # Aqui, senha é a senha do e-mail de envio, provavelmente.

            if not email_usuario or not senha or not corpo_email:
                flash("Todos os campos devem ser preenchidos!", "error")
                return render_template("suport.html")

            # Criar a mensagem de e-mail
            msg = Message()
            msg.set_payload(corpo_email)  # Definir o corpo do e-mail com a mensagem do usuário
            msg["Subject"] = f"Suporte solicitado por: {email_usuario}"
            msg["From"] = email_usuario  # O e-mail de origem será o que o usuário forneceu
            msg["To"] = "gdepaulabaroni@gmail.com"  # E-mail da empresa (destinatário)

            # Enviar o e-mail
            try:
               # Usando SMTP do Gmail
                with smtplib.SMTP("smtp.gmail.com", 587) as s:
                    s.starttls()  # Iniciar comunicação segura
                    s.login(email_usuario, senha)  # Login no e-mail de origem
                    s.sendmail(msg["From"], [msg["To"]], msg.as_string())  # Enviar o e-mail

                flash("Sua mensagem foi enviada com sucesso!", "success")
                return redirect("/suport")
            except Exception as e:
                flash(f"Ocorreu um erro ao enviar o e-mail: {e}", "error")
                return render_template("suport.html")

        return render_template("suport.html")
    
    #Rota para a tela de Reservas do usuário
    @app.route("/reserva_user", methods=["POST", "GET"])
    def reserva_user():
        usuario_id = session.get("usuario_id")
        if not usuario_id:
            flash("Você precisa estar logado para acessar esta página.")
            return redirect(url_for("login")) 
        try:
            user_response = supabase.table("Reserva").select("*").eq("usuario_id", usuario_id).execute()
            if user_response.data:
                reservas = user_response.data
                for reserva in reservas:
                    quarto_id = reserva.get("quarto_id")  # Supondo que a chave do quarto seja "quarto_id"
                    quarto_response = supabase.table("Quarto").select("*").eq("id", quarto_id).execute()
                    if quarto_response.data:
                        reserva['quarto'] = quarto_response.data[0]  # Adiciona o quarto relacionado à reserva

                return render_template("reserva_user.html", reservas=reservas)
            else:
                flash( "Nenhuma reserva encontrada para este usuário.")
                return render_template("reserva_user.html", reservas=[])
        except Exception as e:
            flash("Erro ao acessar os dados. Por favor, tente novamente.")
            return render_template("reserva_user.html", reservas=[], error=str(e))
        


    
