# El módelo de base de datos

Los datos que guardamos en nuestra base de datos serán representados por una colección de clases que son referidas como modelos de base de datos. 

## Definción del modelo

Fichero model.py

## Juagando con el modelo

## Manejando la base de datos con manage.py

## Creación de datos de prueba en nuetra base de datos


juegos=[
    {"nombre":"PAC-MAN","precio":12,"descripcion":"juego de fantasmitas","stock":1,"CategoriaId":1},
    {"nombre":"Super Mario Bros","precio":25,"descripcion":"juego de plataforma","stock":5,"CategoriaId":1}
    ]


    In [1]: from aplicacion.app import db

db.create_all()

from aplicacion.model import Categorias,Articulos

cat=Categorias(nombre="Arcade")

db.session.add(cat)

art1=Articulos(nombre="PAC-MAN",precio=12,descripcion="juego de fantasmitas",stock=1,CategoriaId
    ...: =1)

In [12]: 

In [12]: art2=Articulos(nombre="Super Mario Bros",precio=25,descripcion="juego de platoformas",stock=10,C
    ...: ategoriaId=1)

In [13]: db.session.add_all([art1,art2])

In [14]: db.session.commit()
