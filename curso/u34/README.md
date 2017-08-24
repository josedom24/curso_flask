# Despliegue de aplicación flask en hosting pythonanywhere

En este ejemplo vamos a desplegar nuestra aplicación en un hosting que nos permite trabajar con python llamado [PythonAnywhere](https://www.pythonanywhere.com/), que nos ofrece distintos [planes de contratación](https://www.pythonanywhere.com/pricing/), aunque nosotros vamos a usar el **Beginner** que es gratuito y para aplicaciones de prueba con pocos accesos es suficiente.

## Configuración de la base de datos

PythonAnywhere nos da la posibilidad de trabajar con mysql y con postgres. En nuestro caso en la pestaña `Databases` del dashboard, vamos a crear una base de datos mysql con una base de datos: `josedom24$tienda`:

![bd](img/bd.png)

Por lo tanto tendremos que configurar nuestra aplicación, para indicar la nuevas credenciales de la base de datos, para ello modificamos el fichero `confi.py`:

	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://josedom24:usuario1234@josedom24.mysql.pythonanywhere-services.com/josedom24$tienda'

## Configuración de nuestra aplicación

En este ejemplo vamos a modificar el fichero `app.wsgi` para indicar el directorio de trabajo, además no vamos activar el entrono virtual:

	import sys
	sys.path.insert(0, '/home/josedom24/tienda_videojuegos')
	from aplicacion.app import app as application

## Despliegue de nuestra aplicación

En la pestaña `Consoles` de PythonAnywhere podemos abrir consolas con los distintos interpretes python, con bash o con mysql, vamos a abrir una consola bash para comenzar el despliegue:

![consoles](img/consoles.png)

![consoles2](img/consoles2.png)

Vamos a clonar nuestro repositorio, crear un repositorio e instalar las dependencias:

	$ git clone https://github.com/josedom24/tienda_videojuegos.git -b pythonanywhere
	$ mkvirtualenv --python=/usr/bin/python3.4 flask
	$ workon flask
	(flask)$ pip install -r tienda_videojuegos/requirements.txt

A continuación podemos crear las tablas, cargar los datos de ejemplo y crear el administrador:

	(flask)$ cd tienda_videojuegos
	(flask)$ python3 manage.py create_tables
	(flask)$ python3 manage.py add_data_tables
	(flask)$ python3 manage.py create_admin

Nota: Si queremos modificar cualquier fichero de nuestro proyecto lo podemos hacer desde la pestaña `Files`.

## Creando una nueva aplicación

Por último en la pestaña `Web` tenemos que crear una nueva aplicación:

Elegimos la opción "Manual configuration" para poder indicar el entorno virtual que hemos creado:

![web1](img/web1.png)

Elegimos la versión de python (en este caso la misma con la que hemos creado el entorno virtual, python 3.4) y ya tenemos la aplicación creada. Sólo nos queda indicar la ruta donde se encuentra nuetro entorno virtual, en la sección **Virtualenv**:

![web2](img/web2.png)

Y modificar el fichero ` /var/www/josedom24_pythonanywhere_com_wsgi.py
` en el apartado "WSGI configuration file:" de la sección "Code":

![web3](img/web3.png)

Por útimo reinicimaos el servidor pulsando el botón "Reload ..." y accedemos a la página:

![web4](img/web4.png)