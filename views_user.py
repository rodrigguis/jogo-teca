"""Module views users"""

from app import app
from flask import render_template, request, redirect, session, flash, url_for # type: ignore
from models import Usuarios
from helpers import FormularioUsuario

@app.route('/login')
def login():
    """ Method page login """
    proxima = request.args.get('proxima')
    
    form = FormularioUsuario() 

    return render_template('login.html', proxima=proxima, form=form)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    """ Method page autenticar """
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()

    if usuario:
        if form.senha.data == usuario.senha:
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