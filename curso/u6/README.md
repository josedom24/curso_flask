# Instalación de flask

Vamos a realizar la instalación de Flask utilizando la herramienta `pip` en un entorno virtual creado con `virtualenv`. La instalación de Flask depende de dos paquetes: [Werkzeug](http://werkzeug.pocoo.org/), una librería WSGI para Python y [jinja2](http://jinja.pocoo.org/docs/2.9/) como motor de plantillas.

## Creando el entorno virtual

Como Flask es compatible con python3 vamos a crear un entorno virtual compatible con la versión 3 del interprete python. Para ello nos aseguremos que tenemos la utilidad instalada:

	# apt-get install python-virtualenv

Y creamos el entorno virtual:

	$ virtualenv -p /usr/bin/python3 flask

Para activar nuestro entorno virtual:

	$ source flask/bin/activate
	(flask)$ 

Y a continuación intalamos Flask:

	(flask)$ pip install Flask

Si nos aparece el siguiente aviso durante la instalación:

	WARNING: The C extension could not be compiled, speedups are not enabled.
    Failure information, if any, is above.
    Retrying the build without the C extension now.

La instalación se realiza bien, pero no se habilita el aumento de rendimiento de jinja2.

Puedes volver a realizar la instalación después de instalar el siguiente paquete:
	
	# apt-get install python-dev

Al finalizar podemos comprobar los paquetes python instalados:

	(flask)$ pip freeze
	Flask==0.12.2
	Jinja2==2.9.6
	MarkupSafe==1.0
	Werkzeug==0.12.2
	click==6.7
	itsdangerous==0.24

Podemos guardar las dependencias en un fichero `requirements.txt`:

	# pip freeze > requirements.txt

Para posteriormente poder crear otro entrono virtual con los mismos paquetes:

	# pip install -r requirements.txt

Y finalmente comprobamos la versión de flask que tenemos instalada:

	(flask)$ flask --version
	Flask 0.12.2
	Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
	[GCC 4.9.1]
