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
@app.route('/categoria/<id>')
def inicio(id=0):
	print(id)
	if id==0:
		arts = db.session.query(Articulos).all()
	else:
		arts = db.session.query(Articulos).filter(Articulos.CategoriaId==id).all()
	cats=db.session.query(Categorias).all()
	return render_template('aplicacion/index.html', arts=arts, cats=cats)		

