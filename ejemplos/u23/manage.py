from flask_script import Manager
from aplicacion.app import app,db
from aplicacion.models import *
	
manager = Manager(app)
app.config['DEBUG'] = True # Ensure debugger will load.

@manager.command
def create_tables():
    "Create relational database tables."
    db.create_all()

@manager.command
def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA."
    db.drop_all()

@manager.command
def add_data_tables():
    db.create_all()

    categorias = ("Deportes","Arcade","Carreras","Acción")

    for cat in categorias:
    	categoria=Categorias(nombre=cat)
    	db.session.add(categoria)
    	db.session.commit()

    juegos=[
    {"nombre":"Fifa 2017","precio":65,"descripcion":"juego de futbol","image":"fifa07.jpg","stock":10,"CategoriaId":1},
    {"nombre":"PES 2017","precio":35,"descripcion":"juego de futbol","image":"pes2017.jpg","stock":7,"CategoriaId":1},
    {"nombre":"PAC-MAN","precio":12,"descripcion":"juego de fantasmitas","image":"pacman.jpg","stock":1,"CategoriaId":2},
    {"nombre":"Super Mario Bros","precio":25,"descripcion":"juego de plataforma","image":"supermariobros.png","stock":5,"CategoriaId":2},
    {"nombre":"Need for Spped","precio":25,"descripcion":"juego de carreras","image":"needforspeed.jpg","stock":10,"CategoriaId":3},
    {"nombre":"Out Run","precio":15,"descripcion":"juego de coches","image":"outrun.jpg","stock":3,"CategoriaId":3},
    {"nombre":"Destiny","precio":75,"descripcion":"juego de disparos y acción","image":"destiny.jpg","stock":8,"CategoriaId":4},
    {"nombre":"Metal Gear","precio":65,"descripcion":"juego de acción","image":"metalgear.jpg","stock":10,"CategoriaId":4},
    
    ]
    for jue in juegos:
       	juego=Articulos(**jue)
       	db.session.add(juego)
       	db.session.commit()

	
if __name__ == '__main__':
	manager.run()

