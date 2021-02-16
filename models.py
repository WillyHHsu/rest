from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date

Base = declarative_base()
class Tournament(Base):
    __tablename__ = "public.tournament"
    ID_TOURNAMENT = Column(Integer, primary_key=True, index=True)
    NAME_TOURNAMENT = Column(String, unique=True)
    DATE_INCLUSION = Column(Date, unique=False)
    
class Player(Base):
    __tablename__ = "public.player"
    ID_PLAYER = Column(Integer, primary_key=True, index=True)
    NAME_PLAYER = Column(String, unique=True)
    DATE_INCLUSION = Column(Date, unique=False)
   
class Register(Base):
    __tablename__ = "public.register"
    ID_REGISTER = Column(Integer, primary_key=True, index=True)
    ID_PLAYER = Column(Integer, ForeignKey("public.player.ID_PLAYER"))
    ID_TOURNAMENT = Column(Integer, ForeignKey("public.tournament.ID_TOURNAMENT"))
    DATE_INCLUSION = Column(Date, unique=False)

class Game(Base):
    __tablename__ = "public.game"
    ID_GAME = Column(Integer, primary_key=True, index=True)
    ID_REGISTER = Column(Integer, ForeignKey("public.register.ID_REGISTER"))
    ID_TOURNAMENT = Column(Integer, ForeignKey("public.tournament.ID_TOURNAMENT"))
    ID_PLAYER1 = Column(Integer, ForeignKey("public.player.ID_PLAYER"))
    ID_PLAYER2 = Column(Integer, ForeignKey("public.player.ID_PLAYER"))
    MATCH_RESULT = Column(String,unique=False)
    DATE_INCLUSION = Column(Date, unique=False)


