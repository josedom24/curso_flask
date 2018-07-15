# -*- coding: utf-8 -*-
def application(environ, start_response):
    if environ["PATH_INFO"] == "/":
        respuesta = "<p>Página inicial</p>"
    elif environ["PATH_INFO"] == "/hola":
        respuesta = "<p>Bienvenidos a mi página web</p>"
    else:
        respuesta = "<p><trong>Página incorrecta</strong></p>"
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return respuesta

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
