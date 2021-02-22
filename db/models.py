from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date

Base = declarative_base()


class Tournament(Base):
    __tablename__ = "tournament"
    id_tournament = Column(Integer, primary_key=True, index=True)
    name_tournament = Column(String, unique=True)
    date_inclusion = Column(Date, unique=False)


class Player(Base):
    __tablename__ = "player"
    id_player = Column(Integer, primary_key=True, index=True)
    name_player = Column(String, unique=True)
    date_inclusion = Column(Date, unique=False)


class Register(Base):
    __tablename__ = "register"
    id_register = Column(Integer, primary_key=True, index=True)
    id_player = Column(Integer, ForeignKey("player.id_player"))
    id_tournament = Column(Integer, ForeignKey(
        "tournament.id_tournament"))
    date_inclusion = Column(Date, unique=False)


class Game(Base):
    __tablename__ = "game"
    id_game = Column(Integer, primary_key=True, index=True)
    id_register = Column(Integer, ForeignKey("register.id_register"))
    id_tournament = Column(Integer, ForeignKey(
        "tournament.id_tournament"))
    id_player1 = Column(Integer, ForeignKey("player.id_player"))
    id_player2 = Column(Integer, ForeignKey("player.id_player"))
    match_result = Column(String, unique=False)
    date_inclusion = Column(Date, unique=False)
