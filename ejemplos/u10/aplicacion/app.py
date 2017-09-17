from flask import Flask, request
app = Flask(__name__)	

@app.route('/')
def inicio():
    return 'Página principal'

@app.route('/articulos/')
def articulos():
    return 'Lista de artículos'

@app.route('/articulos/new',methods=["POST"])
def articulos_new():
	return 'Está URL recibe información de un formulario con el método POST'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Hemos accedido con POST'
    else:
        return 'Hemos accedido con GET'

