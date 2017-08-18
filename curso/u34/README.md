pythonanywhere

wsgi:

import sys
sys.path.insert(0, '/home/josedom24/tienda_videojuegos')
from aplicacion.app import app as application

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://josedom24:usuario1234@josedom24.mysql.pythonanywhere-services.com/josedom24$tienda'

Desde una consola bash:

git clone https://

mkvirtualenv --python=/usr/bin/python3.4 my-virtualenv flask
workon flask
pip install -r

(flask)$ python3 manage.py create_tables
(flask)$ python3 manage.py add_data_tables
(flask)$ python3 manage.py create_admin

Go to the Web Tab and hit Add a new web app. Choose Manual Configuration, and then choose the Python version -- make sure it's the same version as the one you used in your virtualenv

Now go to the Virtualenv section, and enter your virtualenv name: my-virtualenv. When you hit enter, you'll see it updates to the full path to your virtuaelenv (/home/yourusername/.virtualenvs/my-virtualenv).

Finally, go edit the wsgi configuration file. You'll find a link to it near the top of the Web tab.