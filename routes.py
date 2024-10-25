from flask import render_template, request, redirect, url_for
import supabase 

# Vou colocar aqui as rotas do site
def init_routes(app):
    @app.route("/")
    def homepage():
        return render_template("index.html")

    @app.route("/login_cadastro", methods=["GET", "POST"])
    def login_cadastro():
        if request.method == "POST":
            #Pegar os dados do formulário
            nome = request.form.get("nome")
            email = request.form.get("email")
            senha = request.form.get("senha")
            tel = request.form.get("tel")

            # Cria um dicionário com os dados do usuário
            data = {
                "Nome": nome,
                "email": email,
                "senha": senha,
                "tel": tel
            }

            # Inserir dados no banco de dados do Supabase
            response = supabase.table("User").insert(data).execute()

            # Verifica o código de status da resposta
            if response.status_code == 201:  # Sucesso
                return redirect(url_for('homepage'))  # Corrigido: usa o nome da função
            else:
                return "Erro ao cadastrar usuário", 400
        else:
            # Renderiza o formulário se o método for GET
            return render_template("login_cadastro.html")
