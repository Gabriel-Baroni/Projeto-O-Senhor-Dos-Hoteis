from flask import Flask 
import os
from supabase import create_client, Client
from routes import init_routes
 


app= Flask(__name__)


#Configuração do Supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

init_routes(app, supabase)

if __name__ == "__main__":
    app.run()
