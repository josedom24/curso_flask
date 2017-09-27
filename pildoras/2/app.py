from flask import Flask
app = Flask(__name__)	

@app.route('/')
def hello_world():
	return '<h1>Hello, World!</h1>'

@app.route('/articulos/')
def articulos():
	return '<h1>Lista de artículos</h1>'	

@app.route('/acercade')
def acercade():
	return '<h1>Página acerca de...<h1>'

@app.route("/articulos/<id>")
def mostrar_ariculo(id):
	return '<h1>Vamos a mostrar el artículo con id:{}</h1>'.format(id)


@app.errorhandler(404)
def page_not_found(error):
	return '<h1>Página no encontrada...</h1>', 404

if __name__ == '__main__':
	app.run('0.0.0.0',5000, debug=True)
