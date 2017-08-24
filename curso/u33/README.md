# Despliegue de aplicación flask en un servidor LAMP

Vamos a desplegar nuestra aplicación web desarrollada con flask en un servidor LAMP (Linux+Apache2+mysql+python) en un sistema operativo GNU/Linux Ubuntu 16.04.

## Configuración del servidor 

Después de actualizar los paquetes del sistema:

	$ sudo apt-get update
	$ sudo apt-get upgrade

Hacemos la instalación del servidor web y del servidor de bases de datos:

	$ sudo apt-get install apache2 mysql-server libapache2-mod-wsgi-py3

## Configuración de la base de datos

Vamos a crear un usuario y una base de datos con la que vamos a a trabajar:

	$ mysql -u root -p

	mysql> create database tienda;
	mysql> GRANT ALL ON tienda.* TO usuario IDENTIFIED BY 'usuario';


Además vamos a configurar nuestra aplicación para que trabaje con mysql, para ello en el fichero `aplicacion\config.py` modificamos el motor de base de datos con el que vamos a trabajar, indicando las credenciales del usuario y la base de datos:

	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ususario:usuario@localhost/tienda'

Por último añadimos en el fichero `requirements.txt` el paquete que me permite que python trabaje con mysql:

	...
	PyMySQL==0.7.11

## Despliegue de la aplicación:

clonamos la rama `lamp` del repositorio: `https://github.com/josedom24/tienda_videojuegos.git`, lo hacemos como superusuario en el directorio `/var/www/html`:

	$ sudo su -
	$ cd /var/www/html
	$ git clone https://github.com/josedom24/tienda_videojuegos.git -b lamp

Como usuario sin privilegios vamos a crear un entorno virtual, donde vamos a instalar las dependencias de nuestra aplicación:

	$ sudo apt-get install python-virtualenv
	$ mkdir venv
	$ cd venv/
	~/venv$ virtualenv -p /usr/bin/python3 flask
	~/venv$ source flask/bin/activate
	(flask) ~/venv$ pip install -r /var/www/html/tienda_videojuegos/requirements.txt 

Creamos las tablas, añadimos los datos de ejemplo y creamos al usuario administrador:

	(flask)$ cd /var/www/html/tienda_videojuegos
	(flask)$ python3 manage.py create_tables
	(flask)$ python3 manage.py add_data_tables
	(flask)$ python3 manage.py create_admin


En el directorio `/var/www/html/tienda_viedojuegos` hemos creado nuestra aplicación WSGI en el fichero `app.wsgi`, donde activamos el entorno virtual que hemos creado:

	import sys
	sys.path.insert(0, '/var/www/html/tienda_videojuegos')
	activate_this = '/home/ubuntu/venv/flask/bin/activate_this.py'
	with open(activate_this) as file_:
	    exec(file_.read(), dict(__file__=activate_this))	

	from aplicacion.app import app as application	
	
	
Por último configuramos apache2 modificando el virtualhost del fichero /etc/apache2/sites-available/000-default.conf`:
Y configuramos el virtualhost:

	...
	DocumentRoot /var/www/html/tienda_videojuegos/aplicacion
    WSGIDaemonProcess tienda user=www-data group=www-data threads=5
    WSGIScriptAlias / /var/www/html/tienda_videojuegos/app.wsgi

    <Directory /var/www/html/tienda_videojuegos/aplicacion>
        WSGIProcessGroup tienda
        WSGIApplicationGroup %{GLOBAL}
        Require all granted
    </Directory>
    ...

Donde definimos el proceso WSGI con la directiva `WSGIDaemonProcess` e indicamos el fichero donde se encuentra la aplicación WSGI con la directiva `WSGISrctiptAlias`, además de dar los permisos de acceso necesarios.

Terminamos reiniciando el servidor:

	$ sudo service apache2 restart

Y probando el acceso a la aplicación:

![web](img/web.png)