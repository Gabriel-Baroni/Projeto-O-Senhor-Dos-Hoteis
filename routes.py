from flask import render_template, request, redirect, url_for, Blueprint, session, flash
from datetime import datetime

bp = Blueprint('main', __name__)

def init_routes(app, supabase):

    # Rota para a tela inicial
    @app.route("/", methods=["GET", "POST"])
    def homepage():
        return render_template("index.html")  # Apenas renderiza o formulário

    # Rota para a página de resultados dos quartos (quartos.html)
    @app.route("/quartos", methods=["POST"])
    def quartos():
        numero_pessoas = int(request.form.get("numero_pessoas"))
        checkin = request.form.get("checkin")
        checkout = request.form.get("checkout")
        session["checkin"] = checkin
        session["checkout"] = checkout
        response = supabase.table("Quarto").select("*").gte("capacidade", numero_pessoas).eq("disponiblidade", 1).execute()
        usuario_id = session.get('usuario_id')
        quartos = response.data  
        
        return render_template("quartos.html", quartos=quartos, usuario_id=usuario_id)
    
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

            reserva_data = {
                "usuario_id": usuario_id,
                "quarto_id": quarto_id,
                "checkin": checkin,
                "checkout": checkout,
                "preco_total": preco_total
            }

            # Insere a reserva no banco de dados
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

                if response.data:
                    user = response.data[0]
                    session['usuario_id'] = user['id']
                    flash("Login realizado com sucesso!")
                    return redirect(url_for('homepage'))
                else:
                    flash("Erro no login: usuário não encontrado ou senha incorreta.")
                    return redirect(url_for("login_cadastro"))

        return render_template("login_cadastro.html")
    
    # Rota para a tela de informações do hotel
    @app.route("/about")
    def about():
        return render_template("about.html")
    
    # Rota para a tela de suporte
    @app.route("/suport")
    def suport():
        return render_template("suport.html")
