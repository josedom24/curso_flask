# El módelo de base de datos

Los datos que guardamos en nuestra base de datos serán representados por una colección de clases que son referidas como modelos de base de datos. 

## Definción del modelo

En nuetro proyecto vamos a definir el modelo en el fichero `models.py` que crearemos dentro del directorio de nuestra aplicación (`aplicacion`). Veamos, por ejemplo, el modelo de la tabla de Articulos:

	from sqlalchemy import Boolean, Column , ForeignKey
	from sqlalchemy import DateTime, Integer, String, Text, Float
	from sqlalchemy.orm import relationship
	from aplicacion.app import db
	...
	class Articulos(db.Model):
		"""Artículos de nuestra tienda"""
		__tablename__ = 'articulos'
		id = Column(Integer, primary_key=True)
		nombre = Column(String(100),nullable=False)
		precio = Column(Float,default=0)
		iva = Column(Integer,default=21)
		descripcion = Column(String(255))
		image = Column(String(255))
		stock = Column(Integer,default=0)
		CategoriaId=Column(Integer,ForeignKey('categorias.id'), nullable=False)
		categoria = relationship("Categorias", backref="Articulos")	

		def precio_final(self):
			return self.precio*self.iva/100	

		def __repr__(self):
			return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

Podemos indicar varias cosas importantes:

* Hemos importado el objeto `db` del módulo principal:

		from aplicacion.app import db

* En la variable `__tablename__` inidcamos el nombre de la tabla a la que corresponde esta clase.
* Vamos indicando los distintos campos del modelo utilizando el constructor `db.Column` e indicando el tipo de datos que van a guardar. Podemos indicar los [siguientes tipos de datos](http://docs.sqlalchemy.org/en/latest/core/type_basics.html).
* Además del tipo de datos podemos indicar [los atributos de cada campo](http://docs.sqlalchemy.org/en/latest/core/constraints.html) (`primary_key`, `unique`, `ForeignKey`,...)
* Hemos indicado una relación con el constructor `relationship` esto nos permite relacionar objetos de una clase (registros de una tabla) con los objetos de otra clase que están relacionados. En nuestro caso es una relación uno a uno entre un artículo y su categoría. (En el modelo de categoría puedes ver una relación 1 a N, una categoria tiene varios artículos).
* Por último cómo estamos creando una clase, podemos definir nuevos módulos (`precio_final`) o reescribir los herededaos de la clase madre (`repr`).

## Juagando con el modelo

Vamos a realizar distintas operaciones con nuestro modelo. Lo primero que hay que indicar que debemos importar antes el objeto `db` que representa la base de datos y posteriormente los modelos que vamos a usar:

	from aplicacion.app import db
	from aplicacion.model import Categorias,Articulos

### Creación de las tablas

Para crear las tablas en la base de datos:

	db.create_all()

Está instrucción no actualiza la estrucutra de la base de datos si cambiamos el módelo, por lo tento en esa circunstancia tenemos que borrar las tablas y crearlas de nuevo:

	db.drop_all()
	db.create_all()

Podemos utilizar también la migración de base de datos que me permite, al cambiar el modelo actualizar la estrucutra de la base de datos. Para trabajar con migraciones podemos usar la extensión [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

### Añadiendo registros a las tablas

A continuación vamos a añadir una categoría:

	cat=Categorias(nombre="Arcade")
	db.session.add(cat)
	db.session.commit()

Y dos artículos de esa categoría:

	art1=Articulos(nombre="PAC-MAN",precio=12,descripcion="juego de fantasmitas",stock=1,CategoriaId=1)	

	art2=Articulos(nombre="Super Mario Bros",precio=25,descripcion="juego de platoformas",stock=10,caetgoria=cat)	

	db.session.add_all([art1,art2])
	db.session.commit()

## Manejando la base de datos con manage.py

## Creación de datos de prueba en nuetra base de datos










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

