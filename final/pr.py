from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bd import Articulos
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Use Flask-SQLAlchemy for its engine and session
# configuration. Load the extension, giving it the app object,
# and override its default Model class with the pure
# SQLAlchemy declarative Base class.
db = SQLAlchemy(app)
db.Model = Articulos

ass = db.session.query(Articulos).all()
for a in ass:
	print a.nombre