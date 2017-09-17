from flask import Flask
app = Flask(__name__)	

@app.route('/')
def inicio():
    return 'Página principal'

@app.route('/articulos/')
def articulos():
    return 'Lista de artículos'

@app.route('/acercade')
def acercade():
    return 'Página acerca de...'

@app.route("/articulos/<int:id>")
def mostrar_ariculo(id):
	return 'Vamos a mostrar el artículo con id:{}'.format(id)

@app.route("/hello/")
@app.route("/hello/<string:nombre>")
@app.route("/hello/<string:nombre>/<int:edad>")
def hola(nombre=None,edad=None):
	if nombre and edad:
		return 'Hola, {0} tienes {1} años.'.format(nombre,edad)
	elif nombre:
		return 'Hola, {0}'.format(nombre)
	else:
		return 'Hola mundo'

