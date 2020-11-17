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

def main():
    manager.run()

if __name__ == "__main__":
    main()