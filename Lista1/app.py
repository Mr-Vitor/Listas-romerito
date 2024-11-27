from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo ao Flask!"

@app.route('/sobre')
def sobre():
    return "Esta é a página Sobre"

@app.route('/saudacao/<nome>')
def saudar(nome):
    return f"Olá {nome}, bem-vindo(a) ao Flask!"

#Desafio
@app.route('/login')
def login():
    return "Você fez login na página, confia"