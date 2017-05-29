from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from aplicacion.model import Articulos,Categorias,Usuarios,Base
from aplicacion import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
db.Model = Base

@app.route('/')
def inicio():
	arts = db.session.query(Articulos).all()
	return render_template('aplicacion/index.html', arts=arts)		

#ass = db.session.query(Articulos).all()
#for a in ass:
#	print (a.nombre)
