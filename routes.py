from flask import render_template, request, redirect, url_for, Blueprint, jsonify
from datetime import datetime

bp = Blueprint('main', __name__)

def init_routes(app, supabase):
    #Rota para a tela inicial
    @app.route("/", methods=["GET", "POST"])
    def homepage():
        return render_template("index.html")  # Apenas renderiza o formulário

    # Rota para a página de resultados dos quartos (quartos.html)
    @app.route("/quartos", methods=["POST"])
    def quartos():
        numero_pessoas = int(request.form.get("numero_pessoas"))
        checkin = datetime.strptime(request.form.get("checkin"), "%Y-%m-%d")
        checkout = datetime.strptime(request.form.get("checkout"), "%Y-%m-%d")
        
        # Consulta os quartos no banco de dados (Supabase)
        response = supabase.table("Quarto").select("*").gte("capacidade", numero_pessoas).eq("disponiblidade", 1).execute()
        
        quartos = response.data  # Lista de quartos encontrados
        
        # Renderiza a página quartos.html com os quartos encontrados
        return render_template("quartos.html", quartos=quartos)
    


    #Rota para a tela de login e cadastro
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
                    return redirect(url_for('homepage'))
                else:
                    return f"Erro ao cadastrar usuário: {response}", 400

            elif action == "login":
                email = request.form.get("email")
                senha = request.form.get("senha")

                response = supabase.table("User").select("*").eq("email", email).eq("senha", senha).execute()

                if response.data:
                    return redirect(url_for('homepage'))
                else:
                    return "Erro no login: usuário não encontrado ou senha incorreta", 400

        return render_template("login_cadastro.html")
    
    #Rota para a tela de informações do hotel
    @app.route("/about")
    def about():
        return render_template("about.html")
    
    #Rota para a tela de suporte 
    @app.route("/suport")
    def suport():
        return render_template("suport.html")
    
