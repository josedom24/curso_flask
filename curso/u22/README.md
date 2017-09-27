# El modelo de base de datos

Los datos que guardamos en nuestra base de datos serán representados por una colección de clases que son referidas como modelos de base de datos. 

## Definición del modelo

En nuestro proyecto vamos a definir el modelo en el fichero `models.py` que crearemos dentro del directorio de nuestra aplicación (`aplicacion`). Veamos, por ejemplo, el modelo de la tabla de `Articulos`:

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

* En la variable `__tablename__` indicamos el nombre de la tabla a la que corresponde esta clase.
* Vamos indicando los distintos campos del modelo utilizando el constructor `db.Column` e indicando el tipo de datos que van a guardar. Podemos indicar los [siguientes tipos de datos](http://docs.sqlalchemy.org/en/latest/core/type_basics.html).
* Además del tipo de datos podemos indicar [los atributos de cada campo](http://docs.sqlalchemy.org/en/latest/core/constraints.html) (`primary_key`, `unique`, `ForeignKey`,...)
* Hemos indicado una relación con el constructor `relationship`, esto nos permite relacionar objetos de una clase (registros de una tabla) con los objetos de otra clase que están relacionados. En nuestro caso es una relación uno a uno entre un artículo y su categoría. (En el modelo de categoría puedes ver una relación 1 a N, una categoría tiene varios artículos).
* Por último cómo estamos creando una clase, podemos definir nuevos métodos (`precio_final`) o reescribir los heredados de la clase madre (`repr`).

## Jugando con el modelo

Vamos a realizar distintas operaciones con nuestro modelo. Lo primero que hay que indicar que debemos importar antes el objeto `db` que representa la base de datos y posteriormente los modelos que vamos a usar:

	from aplicacion.app import db
	from aplicacion.models import Categorias,Articulos

### Creación de las tablas

Para crear las tablas en la base de datos:

	db.create_all()

Está instrucción no actualiza la estructura de la base de datos si cambiamos el modelo, por lo tanto en esa circunstancia tenemos que borrar las tablas y crearlas de nuevo:

	db.drop_all()
	db.create_all()

Podemos utilizar también la migración de base de datos que me permite, al cambiar el modelo actualizar la estructura de la base de datos. Para trabajar con migraciones podemos usar la extensión [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

### Añadiendo registros a las tablas

A continuación vamos a añadir una categoría:

	cat=Categorias(nombre="Arcade")
	db.session.add(cat)
	db.session.commit()

Y dos artículos de esa categoría:

	art1=Articulos(nombre="PAC-MAN",precio=12,descripcion="juego de fantasmitas",stock=1,CategoriaId=1)	

	art2=Articulos(nombre="Super Mario Bros",precio=25,descripcion="juego de platoformas",stock=10,categoria=cat)	

	db.session.add_all([art1,art2])
	db.session.commit()


### Modificando registros

Simplemente podemos cambiar el valor de una campo y volver añadirlo:
	
	art1.precio=15
	db.session.add(art1)
	db.session.commit()

### Borrando registros

	db.session.delete(art2)	
	db.session.commit()	

### Obteniendo registros

Podemos realizar [diferentes operaciones](http://docs.sqlalchemy.org/en/latest/orm/query.html) para obtener un conjunto de registros.

Por ejemplo podemos obtener el primer registro:

	art=Articulos.query.first()

O el registro cuyo identificador sea el 2:

	art=Articulos.query.get(2)

O podemos obtener todos los artículos:

	articulos=Articulos.query.all()

Cuando tenemos un registro (que corresponde a un objeto de nuestro modelo) podemos obtener el valor de cada uno de los campos:

	print(art.nombre)

Por lo tanto podemos recorrer todos los registros para mostrar el nombre:

	for art in Articulos.query.all():
    	print (art.nombre)

Para terminar podemos obtener el número de registros:

	Articulos.query.count()

### Filtrando registros

Podemos obtener los artículos que tienen un precio determinado:

	Articulos.query.filter_by(precio=25).all()

Si quiero filtrar por dos campos:

	Articulos.query.filter_by(precio=25).filter_by(iva=21).all()

Si quieres ordenar por un campo:

	Articulos.query.order_by("precio").all()

### Trabajar con las relaciones

A partir de un artículo puedo obtener los datos de la categoría:

	art1.categoria.nombre

Y a partir de una categoría puedo obtener los artículos de la misma:

	for art in cat.articulos:
    	print(art.nombre)

## Manejando la base de datos con manage.py

Vamos a modificar el fichero `manage.py` para añadir nuevas opciones para gestionar nuestra aplicación:

	@manager.command
	def create_tables():
	    "Create relational database tables."
	    db.create_all()	

	@manager.command
	def drop_tables():
	    "Drop all project relational database tables. THIS DELETES DATA."
	    db.drop_all()

De esta manera podemos crear las tablas de nuestra base de datos con esta instrucción:

	python3 manage.py create_tables

Y eliminar las tablas con:

	python3 manage.py drop_tables

Además hemos añadido una nueva función (que puedes ver en el código) para añadir datos de ejemplo:

	python3 manage.py add_data_tables

## Uso del modelo en el programa principal

En esta unidad hemos desarrollado una pequeña vista para mostrar los nombres de los artículos. En el fichero `app.py` tendríamos:

	...
	from aplicacion.models import Articulos
	@app.route('/')
	def inicio():
		articulos=Articulos.query.all()
		return render_template("inicio.html",articulos=articulos)
	...

y la plantilla `inicio.html` quedaría:


	...
	<div class="panel-heading">Videojuegos</div>
  		<table class="table">
  	   		{% for art in articulos %}
  	   			<tr>
  	   				<td>{{art.nombre}}</td>
  	   			</tr>
  	   		{% endfor %}
  		</table>
  	</div>
	...


## Código ejemplo de esta unidad

[Código](../../ejemplos/u22)
