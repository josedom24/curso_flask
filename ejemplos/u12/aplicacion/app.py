from flask import Flask, make_response, abort, redirect,url_for
app = Flask(__name__)	

@app.route('/string/')
def return_string():
    return 'Hello, world!'

@app.route('/object/')
def return_object():
    headers = {'Content-Type': 'text/plain'}
    return make_response('Hello, world!', 200,headers)

@app.route('/tuple/')
def return_tuple():
    return 'Hello, world!', 200, {'Content-Type':'text/plain'}

@app.route('/login')
def login():
    abort(401)

@app.errorhandler(404)
def page_not_found(error):
    return 'Página no encontrada...', 404

@app.route('/')
def index():
    return redirect(url_for('return_string'))

if __name__ == '__main__':
  		app.run('0.0.0.0',8080, debug=True)