sudo apt-get install apache2 mysql-server 

mysql> create database tienda;
Query OK, 1 row affected (0.00 sec)

mysql> GRANT ALL ON tienda.* TO usuario IDENTIFIED BY 'usuario';
Query OK, 0 rows affected, 1 warning (0.00 sec)


En config.py

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ususario:usuario@localhost/tienda'

En requierements.txt

pymysql


En el servidor:


git clone https://github.com/josedom24/tienda_videojuegos.git

$ mkdir venv
ubuntu@ubuntu-xenial:~$ cd venv/
ubuntu@ubuntu-xenial:~/venv$ virtualenv -p /usr/bin/python3 flask
(flask) ubuntu@ubuntu-xenial:~/venv$ pip install -r /var/www/html/tienda_videojuegos/requirements.txt 

Cargamos los datos de las tables:

(flask)$ python3 manage.py create_tables
(flask)$ python3 manage.py add_data_tables
(flask)$ python3 manage.py create_admin


sudo apt-get install libapache2-mod-wsgi-py3

En tienda_viedojuegos creamos app.wsgi

	import sys
	sys.path.insert(0, '/var/www/html/tienda_videojuegos')
	activate_this = '/home/ubuntu/venv/flask/bin/activate_this.py'
	with open(activate_this) as file_:
	    exec(file_.read(), dict(__file__=activate_this))	

	from aplicacion.app import app as application	
	
	
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

