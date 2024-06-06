from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.usuario import Usuario
from flask_sqlalchemy import SQLAlchemy

class Jogo: 
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria = categoria
        self.console = console

    def __str__(self):
        return 

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack in Slash', 'PS2')
jogo3 = Jogo('Crash', 'Rack in Slash', 'PSP')
lista = [jogo1, jogo2, jogo3] 

usuario1 = Usuario("Renato Rodrigues", "Re", "renato")
usuario2 = Usuario("Tania Maria", "Tan", "tania")
usuario3 = Usuario("Allana", "Lana", "allana")

usuarios = {usuario1.nickname : usuario1,
             usuario2.nickname : usuario2, 
             usuario3.nickname : usuario3}


app = Flask(__name__)
app.secret_key = 'alura'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'jogoteca'
    )

db = SQLAlchemy(app)

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome




@app.route('/')
def index(): 
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo(): 
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar(): 
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)

    lista.append(jogo)

    return redirect(url_for('index'))

@app.route('/login')
def login(): 
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar(): 
    if request.form['usuario'] in usuarios: 
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso ')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else: 
        flash('Usuario nao logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout(): 
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')

    return redirect(url_for('index'))

app.run(debug=True)