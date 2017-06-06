from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from os import listdir
from aplicacion.forms import UploadForm
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Bootstrap(app)	

@app.route('/')
def inicio():
	
	lista=[]
	for file in listdir(app.root_path+"/static/img"):
		lista.append(file)
	return render_template("inicio.html",lista=lista)

@app.route('/upload', methods=['get', 'post'])
def upload():
	form= UploadForm() # carga request.from y request.file
	if form.validate_on_submit():
		f = form.photo.data
		filename = secure_filename(f.filename)
		f.save(app.root_path+"/static/img/"+filename)
		return redirect(url_for('inicio'))
	return render_template('upload.html', form=form)	

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
	app.run('0.0.0.0',8080, debug=True)
