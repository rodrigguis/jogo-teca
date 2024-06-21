""" Module principal """

from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_wtf.csrf import CSRFProtect # type: ignore

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from views_game import *
from views_user import *

if __name__ == '__main__':
    app.run(debug=True)
