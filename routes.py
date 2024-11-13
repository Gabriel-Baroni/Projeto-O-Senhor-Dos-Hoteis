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
        response = supabase.table("Quarto").select("*").gte("capacidade", numero_pessoas).eq("disponiblidade", 1).execute()
        usuario_id = session.get('usuario_id')
        quartos = response.data  
        
        return render_template("quartos.html", quartos=quartos, usuario_id=usuario_id)
    
    @app.route("/reserva", methods=["GET", "POST"])
    def reserva():
        pass
    
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
