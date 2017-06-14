# Listando y filtrando los registros de la base de datos

En esta unidad vamos a seguir trabajndo en nuestreo proyecto, vamos a listar los artículos y las categorías. Además vamos a poder seleccionar los artículos por categoria.

## Seleccionando registros en el programa principal

	@app.route('/')
	@app.route('/categoria/<id>')
	def inicio(id='0'):
		categoria=Categorias.query.get(id)
		if id=='0':
			articulos=Articulos.query.all()
		else:
			articulos=Articulos.query.filter_by(CategoriaId=id)
		categorias=Categorias.query.all()
		return render_template("inicio.html",articulos=articulos,categorias=categorias,categoria=categoria)

Ejecutamos esta función cuando accedemos a la página (ruta `/`) o cuando hemos seleccionado una determinada categoria (ruta `categorida/<id>`):

* Si accedemos a la página (ruta `/`) el identificado de la categoría será por defecto el 0, que corresponde a la categoría `Todos`. En este caso se selccionan todos los artículos.
* Si accedemos a la página sleccioanndo una categoría, se mandará el identificador de la categoría y se seleccionarán los videojuegos que tienen dicha categoría.

En los dos casos se muestra una plantilla donde se muestran todas las categorías y los artículos seleccionados.

Consideramos que la categoría 0:'Todos', debe existir al crear las tablas por lo tanto hemos modificado el fichero `manage.py` para crearla:

	@manager.command
	def create_tables():
	    "Create relational database tables."
	    db.create_all()
	    categoria=Categorias(id=0,nombre="Todos")
	    db.session.add(categoria)
	    db.session.commit()

## Plantilla para mostrar el listado: `inicio.html`