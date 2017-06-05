from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")


@app.route("/procesar", methods=["post"])
def procesar_formulario():
	passwd=request.form.get("pass_control")
	if passwd=="asdasd":
		datos = request.form
		return render_template("datos.html",datos=datos)	
	else:
		return render_template("error.html",error="Contraseña incorrecta")

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
	app.run('0.0.0.0',8080, debug=True)
