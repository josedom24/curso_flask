from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from os import listdir




app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Bootstrap(app)	

@app.route('/')
def inicio():
	
	lista=[]
	for file in listdir(app.root_path+"/static/img"):
		lista.append(file)
	return render_template("inicio.html",lista=lista)

@app.route('/upload')
def upload():
	pass
	
@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
	app.run('0.0.0.0',8080, debug=True)
