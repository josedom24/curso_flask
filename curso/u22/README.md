# El módelo de base de datos

Los datos que guardamos en nuestra base de datos serán representados por una colección de clases que son referidas como modelos de base de datos. 

## Definción del modelo

Fichero model.py

## Juagando con el modelo

## Manejando la base de datos con manage.py

## Creación de datos de prueba en nuetra base de datos



from aplicacion.app import db
from aplicacion.model import Categorias,Articulos,Usuarios

db.create_all()
cat=Categorias(nombre="Arcade")
db.session.add(cat)
db.session.commit()

art1=Articulos(nombre="PAC-MAN",precio=12,descripcion="juego de fantasmitas",stock=1,CategoriaId=1)

art2=Articulos(nombre="Super Mario Bros",precio=25,descripcion="juego de platoformas",stock=10,caetgoria=cat)

db.session.add_all([art1,art2])

db.session.commit()


art=Articulos.query.first()
art=Articulos.query.get(2)

Articulos.query.count()
2

Articulos.query.filter_by(precio=25).all()

for art in Articulos.query.all():
   ...:     print (art.nombre)
   ...:     
PAC-MAN
Super Mario Bros

