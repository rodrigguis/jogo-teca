import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from app import app

class FormularioJogo(FlaskForm):
    """Class Formulario"""
    nome = StringField('Name of game: ', [validators.DataRequired(), validators.Length(min=2, max=50)])
    categoria = StringField('Category: ', [validators.DataRequired(), validators.Length(min=2, max=40)])
    console = StringField('Console: ', [validators.DataRequired(), validators.Length(min=2, max=20)])
    salvar = SubmitField('Save')

class FormularioUsuario(FlaskForm): 
    """Class Formulario Usuario"""
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=50)])
    senha = StringField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Salvar')

def recupera_imagem(id):
    """ Method page recupera """

    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'


def deleta_arquivo(id):
    """ Method page deleta """

    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
