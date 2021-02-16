from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper
from fastapi_sqlalchemy import db  # an object to provide global access to a database session

from app.models import Player

app = FastAPI()


@app.get("/users")
def get_users():
    users = db.session.query(Player).all()
    return users

