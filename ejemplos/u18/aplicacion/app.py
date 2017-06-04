from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)	

@app.route('/')
def inicio():
    return render_template("inicio.html")




@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
	app.run('0.0.0.0',8080, debug=True)