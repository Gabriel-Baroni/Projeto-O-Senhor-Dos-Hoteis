from flask import render_template, request, redirect, url_for, Blueprint

bp = Blueprint('main', __name__)

def init_routes(app, supabase):
    @app.route("/")
    def homepage():
        return render_template("index.html")

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
