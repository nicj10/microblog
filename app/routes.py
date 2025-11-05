from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Nicholas"
    idade = 19
    dados = {"profissao": "programador e músico", "rg": "11078220"}
    return render_template('index.html', nome=nome, idade=idade, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')