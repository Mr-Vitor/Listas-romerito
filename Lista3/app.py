from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Página Inicial"

@app.route('/formulario', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        nome = request.form.get('nome')
        comentario = request.form.get('comentario')
        return f"""Obrigado pelo feedback, {nome}!
        Comentário recebido:
        {comentario}"""
    return "Bem-vindo ao formulário! Por favor, envie seu feedback." + render_template('formulario.html')

#Desafio

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        return f"Obrigado {nome}, o email cadastrado foi: {email}"
    return "Faça o seu cadastro em menos de um minuto" + render_template('cadastro.html')