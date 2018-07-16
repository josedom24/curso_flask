# -*- coding: utf-8 -*-
def application(environ, start_response):
    # Guardo la salida que devolveré como respuesta
    respuesta = "<p>Página web construida con <strong>Python!!!</strong></p>"
    # Se genera una respuesta al navegador
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return respuesta

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
