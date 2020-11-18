import click
from flask import Flask
from flask_migrate import Migrate, MigrateCommand

from budget import app, db

migrate = Migrate(app, db)

# Create User
@app.cli.command('create-user')
@click.argument('first_name')
@click.argument('last_name')
@click.argument('email')
@click.argument('username')
@click.argument('password')
def seedUsers(**kwargs):
    from budget.models.users import User
    print(kwargs)
    user = User(
            first_name=kwargs['first_name'],
            last_name=kwargs['last_name'], 
            email=kwargs['email'], 
            username=kwargs['username'], 
            password=kwargs['password']
        )
    user.create()

def main():
    app.run()

if __name__ == "__main__":
    main()