from main import app
from flask import render_template

#Vou colocar aqui as rotas do site

@app.route("/")
def homepage():
    return render_template("index.html")
