from flask import Flask, url_for
app = Flask(__name__)	

@app.route('/')
def inicio():
    return '<img src="'+url_for('static', filename='img/tux.png')+'"/>'


if __name__ == '__main__':
  		app.run('0.0.0.0',8080, debug=True)