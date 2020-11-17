from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand

from budget import app, db

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def drop_db():
    """ Drop the databases """
    db.drop_all()

if __name__ == "__main__":
    manager.run()