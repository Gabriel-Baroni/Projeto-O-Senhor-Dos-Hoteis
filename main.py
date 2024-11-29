from flask import Flask 
import os
from supabase import create_client, Client
from routes import init_routes

#Chave de sessão do Flask
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

app= Flask(__name__)
app.secret_key = FLASK_SECRET_KEY 

#Configuração do Supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)



init_routes(app, supabase)

if __name__ == "__main__":
    app.run()
