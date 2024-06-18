import os
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField

class FormularioJogo(FlaskForm):
    """Class FormularioJogo"""
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=2, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.Length(min=2, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=2, max=20)])
    salvar = SubmitField('Save')


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
