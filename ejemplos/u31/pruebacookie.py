from flask import Flask,request,redirect
app = Flask(__name__)	

@app.route('/')
def inicio():
	return "Inicio"

@app.route('/set_cookie')
def set_cookie():
    redirect_to_index = redirect('/')
    response = app.make_response(redirect_to_index )  
    response.set_cookie('cookie_name',value='Tenemos una cookie')
    return response

@app.route('/get_cookie')
def get_cookie():
    datos = request.cookies.get('cookie_name')
    if datos!=None:
        return datos
    else:
        return "No hay cookie"

@app.route('/del_cookie')
def del_cookie():
    redirect_to_index = redirect('/')
    response = app.make_response(redirect_to_index )  
    response.set_cookie('cookie_name',value='',expires=0)
    return response

if __name__ == '__main__':
  		app.run('0.0.0.0',8080, debug=True)