sudo apt-get install apache2 mysql-server

mysql> create database tienda;
Query OK, 1 row affected (0.00 sec)

mysql> GRANT ALL ON tienda.* TO usuario IDENTIFIED BY 'usuario';
Query OK, 0 rows affected, 1 warning (0.00 sec)


En config.py

SQLALCHEMY_DATABASE_URI = 'mysql://ususario:usuario@localhost/tienda'

En requierements.txt

python-mysql


En el servidor:


git clone https://github.com/josedom24/tienda_videojuegos.git

$ mkdir venv
ubuntu@ubuntu-xenial:~$ cd venv/
ubuntu@ubuntu-xenial:~/venv$ virtualenv -p /usr/bin/python3 flask
(flask) ubuntu@ubuntu-xenial:~/venv$ pip install -r /var/www/html/tienda_videojuegos/requirements.txt 
