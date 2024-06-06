""" Module principal """


from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

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
    """ Class ORM representa Jogos """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Usuarios(db.Model):
    """ Class ORM representa Usuarios """

    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


@app.route('/')
def index():
    """ Method page index """

    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    """ Method page novo """

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))

    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    """ Method page criar """

    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogo ja existente!')
        return redirect(url_for('index'))

    novo_jog = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jog)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/login')
def login():
    """ Method page login """

    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    """ Method page autenticar """

    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()

    if usuario:
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
    """ Method page logout """

    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')

    return redirect(url_for('index'))


app.run(debug=True)