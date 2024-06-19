""" Modulo Views """

from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from app import app, db
from models import Jogos, Usuarios
from helpers import recupera_imagem, deleta_arquivo, FormularioJogo
import time


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

    form = FormularioJogo()

    return render_template('novo.html', titulo='Novo Jogo', form=form)


@app.route('/criar', methods=['POST',])
def criar():
    """ Method page criar """
    form = FormularioJogo(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogo ja existente!')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    # timestamp = time.time()
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    arquivo.save(f'{upload_path}/capa{novo_jogo.id}-{timestamp}.jpg')

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


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    """ Method page imagem """
    return send_from_directory('uploads', nome_arquivo)


@app.route('/editar/<int:id>')
def editar(id):
    """ Method page editar """
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))

    jogo = Jogos.query.filter_by(id=id).first()
    capa_jogo = recupera_imagem(id)

    return render_template('editar.html', titulo='Edicao Jogo', jogo=jogo, capa_jogo=capa_jogo)


@app.route('/atualizar', methods=['POST',])
def atualizar():
    """ Method page atualizar """
    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    # timestamp = time.time()
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    deleta_arquivo(jogo.id)
    arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')

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



