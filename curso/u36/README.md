# Despliegue de aplicación flask en un contenedor docker

Vamos a desplegar nuestra aplicación web desarrollada con flask en docker. Vamos a utilizar dos contenedores: uno para la base de datos mysql y otro para nuestra aplicación.

Seguimos las [instrucciones de la documentación de docker](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) para realizar la instalación en Ubuntu 16.04.

## Contenedor de base de datos

Vamos a arrancar un contenedor que nos sirva la base de datos, indicamos la contraseña del usuario root y creamos una base de datos:

	sudo docker run --name servidor_mysql -e MYSQL_DATABASE=tienda -e MYSQL_ROOT_PASSWORD=asdasd -d mysql

En al configuración de la conexión a la base de datos de nuestra aplicación, en el fichero `config.py` tendremos que indicar los parámetros de conexión y la contraseña del root de mysql que vamos a mandar cunado creemos el contenedor, de la siguiente manera:

	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@{}/tienda'.format(os.environ["MYSQL_PASSWORD"],os.environ["MYSQL_PORT_3306_TCP_ADDR"])

## Creando la imagen para el contenedor de nuestra aplicación

Clonamos la rama ocker` del repositorio github donde tenemos los ficheros de nuestra aplicación:

	$ git clone https://github.com/josedom24/tienda_videojuegos.git -b docker

En el repositorio tenemos un fichero `Dockerfile` donde definimos las instrucciones que vamos a ejecutar para crear la imagen docker:

	FROM ubuntu:16.04
	MAINTAINER José Domingo Muñoz
	RUN apt-get update -y && apt-get install -y \
	        apache2 \
	        libapache2-mod-wsgi-py3 \
	        python3-pip \
	        && apt-get clean && rm -rf /var/lib/apt/lists/*
	ADD /tienda_videojuegos /var/www/html/tienda_videojuegos
	RUN chown www-data:www-data -R /var/www/html/tienda_videojuegos
	RUN pip3 install -r /var/www/html/tienda_videojuegos/requirements.txt
	ADD 000-default.conf /etc/apache2/sites-available/
	ADD app.wsgi /var/www/html/tienda_videojuegos
	RUN service apache2 restart
	ENV APACHE_RUN_USER www-data
	ENV APACHE_RUN_GROUP www-data
	ENV APACHE_LOG_DIR /var/log/apache2
	EXPOSE 80
	WORKDIR /var/www/html/tienda_videojuegos
	COPY ./run.sh /
	ENTRYPOINT ["/run.sh"]


También tenemos el fichero donde creamos la aplicación WSGI, `app.wsgi`:

	import sys
	sys.path.insert(0, '/var/www/html/tienda_videojuegos')
	from aplicacion.app import app as application

El fichero de configuración del virtualhost de apache2: `000-default.conf`:

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

Y por último el fichero `run.sh` que el script que se va a ejecutar cuando creemos el contenedor:

	#!/bin/bash
	python3 manage.py create_tables
	python3 manage.py add_data_tables
	/usr/sbin/apache2ctl -D FOREGROUND

Creamos las tablas con los datos de ejemplo de la base de datos y ejecutamos el servidor apache2.

Para crear la imagen ejecutamos el siguiente comando:

	$ cd tienda_videojuegos
	$ sudo docker -t tienda .

Y comprobamos que hemos generado la nueva imagen:

	$ sudo docker image ls
	REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
	tienda              latest              bb1d87c90448        46 hours ago        474MB
	ubuntu              16.04               ccc7a11d65b1        11 days ago         120MB
	mysql               latest              c73c7527c03a        3 weeks ago         412MB


## Contenedor con nuestra aplicación

Para crear el contenedor con nuestra aplicación:

	$ sudo docker run --name mytienda -e MYSQL_PASSWORD=asdasd -p 8080:80 --link servidor_mysql:mysql -d tienda

Comprobamos que los contenedores se están ejecutando:

	$ sudo docker ls
	CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
	08eadf7d87b0        tienda              "/run.sh"                4 seconds ago       Up 3 seconds        0.0.0.0:8080->80/tcp   mytienda
	6ccff57702ba        mysql               "docker-entrypoint..."   16 seconds ago      Up 16 seconds       3306/tcp               servidor_mysql


Si queremos crear el usuario administrador de nuestra aplicación podemos acceder de forma interactiva a nuestro contendor para ejecutar la instrucción necesaria:
	
	$ sudo docker exec -i -t mytienda /bin/bash	
	root@5db96abf79b3:/var/www/html/tienda_videojuegos# python3 manage.py create_admin

Por ultimo comprobamos que la aplicación está funcionando accediendo a la ip del servidor y al puerto 8080:

![web](img/web.png)