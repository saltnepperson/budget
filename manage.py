from flask import Flask
from flask_migrate import Migrate, MigrateCommand

from budget import app, db

migrate = Migrate(app, db)

def main():
    app.run()

if __name__ == "__main__":
    main()