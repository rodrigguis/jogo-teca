""" Modulo Views """

from flask import render_template, request, redirect, session, flash, url_for
from app import app, db
from models import Jogos, Usuarios

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


@app.route('/editar/<int:id>')
def editar(id):
    """ Method page editar """

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))

    jogo = Jogos.query.filter_by(id=id).first()

    return render_template('editar.html', titulo='Edicao Jogo', jogo=jogo)


@app.route('/atualizar', methods=['POST',])
def autalizar():
    """ Method page atualizar """

    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    """ Method delete """

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash(f'Jogo {Jogos.id} deletado com sucesso!')

    return redirect(url_for('index'))

