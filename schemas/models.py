from datetime import datetime
from pydantic import BaseModel


class Tournament(BaseModel):
    name_tournament: str
    date_inclusion: datetime


class Player(BaseModel):
    id_player: int
    name_player: str
    date_inclusion: datetime


class Register(BaseModel):
    id_register: int
    id_player: int
    id_tournament: int
    date_inclusion: datetime


class Game(BaseModel):
    id_game: int
    id_register: int
    id_tournament: int
    id_player1: int
    id_player2: int
    match_result: str
    date_inclusion: datetime
