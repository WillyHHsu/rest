import os
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from dotenv import load_dotenv
from sqlalchemy import schema

from db import models as db_model
from schemas import models as schema

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_URL = os.getenv('POSTGRES_URL')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)

app = FastAPI(
    title="API REST",
    description="Uma API REST by WillyHHsu",
)

app.add_middleware(
    DBSessionMiddleware,
    db_url=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_URL}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

@app.get("/users")
def get_users():
    users = db.session.query(db_model.Player).all()
    return users


@app.post("/tournament",
          summary='Cadastra um novo torneio',
          response_model=schema.Tournament)
def new_tournament(tornament_request: schema.Tournament):
    db.session.add(db_model.Tornament(tornament_request))
    db.session.commit()
    return schema.Tournament(**tornament_request)


@app.post("/tournament/{id_tournament}/competitor",
          summary='Cadastra um novo competidor')
def new_tournament(id_tournament):
    return db.session.query(db_model.Tournament).filter(id_tournament=id_tournament).first()


@app.get("/tournament/{id_tournament}/match",
         summary='Lista as partidas de um torneio')
def list_match(id_tournament):
    return db.session.query(db_model.Game).filter(id_tournament=id_tournament).all()
