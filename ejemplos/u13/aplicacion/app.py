from flask import Flask, url_for
app = Flask(__name__)	

@app.route('/')
def inicio():
    return '<img src="'+url_for('static', filename='img/tux.png')+'"/>'


