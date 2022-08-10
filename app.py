from flask import Flask

app = Flask(__name__)

@app.route('/pagina1')
def hello():
    return "<h1>Meu Primeiro Site em Python</h1>"

@app.route("/contatos")
def contato():
    return "Bibi"