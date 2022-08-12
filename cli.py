import typer
import alembic.config
import os

app = typer.Typer()

@app.command()
def say_hello():
    """
    Say hello to
    """
    nama = typer.prompt("what's your name: ")
    print(f"hello {nama}")


@app.command()
def refresh_initial():
    """
    Drop All Migration -> Migrate Database -> initial-data
    """
    alembic_args = ["downgrade", "base"]
    alembic.config.main(argv=alembic_args)
    alembic_args = ["upgrade", "head"]
    alembic.config.main(argv=alembic_args)

@app.command()
def create_app():
    name = typer.prompt("what's your app name: ")

    app = str(name)    
    os.mkdir(app)
    open(f'{app}/__init__.py','x')
    open(f'{app}/endpoints.py','x')
    open(f'{app}/model.py','x')
    open(f'{app}/repository.py','x')
    open(f'{app}/schemas.py','x')
    open(f'{app}/services.py','x')
    open(f'{app}/{app}_test.py','x')

    pythonic_app = app[0].upper()+app[1:]

    f = open(f'{app}/__init__.py','w')
    f.write(f'''from fastapi import APIRouter \nfrom .endpoints import router as {app} \n\n{app}_router = APIRouter(prefix='/{app}')\n{app}_router.include_router({app})''')
    f.close()

    f = open(f'{app}/endpoints.py','w')
    f.write(f'''from fastapi import APIRouter, Depends \nfrom common.responses_schemas import BadRequest, InternalServerError,Forbidden \nfrom common.responses_services import common_response \nfrom .services import {pythonic_app}Services \n\nrouter = APIRouter(\n    tags=['{app}']\n) \n\n  #create endpoints here :)''')
    f.close()

    f = open(f'{app}/model.py','w')
    f.write(f'''from sqlalchemy import Column \nfrom database import Base \n\nclass {pythonic_app}(Base):\n __tablename__ = '{app}' \n\n   #create columns here =)''')
    f.close()

    f = open(f'{app}/repository.py','w')
    f.write(f'''from .model import User \nfrom sqlalchemy import select \nfrom database import Session \n\nclass {pythonic_app}Repository:\n  pass''')
    f.close()

    f = open(f'{app}/schemas.py','w')
    f.write(f'''from pydantic import BaseModel''')
    f.close()

    f = open(f'{app}/services.py','w')
    f.write(f'''from .repository import {pythonic_app}Repository \nfrom .model import {pythonic_app} \nfrom common.responses_services import BadRequest,Created,InternalServerError, Ok \nfrom common.security import generate_jwt_token_from_user \n\nclass {pythonic_app}Services:\n  pass # add your services here :`) ''')
    f.close()

    f = open(f'{app}/{app}_test.py','w')
    f.write(f'''from unittest import IsolatedAsyncioTestCase \n\nclass Test{pythonic_app}App(IsolatedAsyncioTestCase):\n pass # add you unittest <3''')
    f.close()

    print(f'your {name}App created, lets code !!!')
    

if __name__ == "__main__":
    app()
