from flask_script import Manager
from aplicacion.app import app,db
manager = Manager(app)


@manager.command
def create_tables():
    "Create relational database tables."
    db.create_all()

@manager.command
def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA."
    db.drop_all()

app.config['DEBUG'] = True # Ensure debugger will load.
if __name__ == '__main__':
	manager.run()