CREATE SEQUENCE tournament_id_seq;
CREATE SEQUENCE player_id_seq;
CREATE SEQUENCE register_id_seq;
CREATE SEQUENCE game_id_seq;

CREATE TABLE public.tournament (
    ID_TOURNAMENT integer DEFAULT nextval('tournament_id_seq') PRIMARY KEY,
    NAME_TOURNAMENT varchar(250)  not null,
    DATE_INCLUSION date not null
);

CREATE TABLE public.player (
    ID_PLAYER integer DEFAULT nextval('tournament_id_seq') PRIMARY KEY,
    NAME_PLAYER varchar(100)  not null,
    DATE_INCLUSION date not null
);

CREATE TABLE public.register (
    ID_REGISTER integer DEFAULT nextval('register_id_seq') PRIMARY KEY,
    ID_PLAYER integer REFERENCES player (ID_PLAYER),
    ID_TOURNAMENT integer  REFERENCES tournament(ID_TOURNAMENT), 
    DATE_INCLUSION date not null

);

CREATE TABLE public.game (
	ID_GAME integer DEFAULT nextval('game_id_seq') PRIMARY KEY,
	ID_REGISTER integer REFERENCES register (ID_REGISTER),
    ID_TOURNAMENT integer REFERENCES tournament (ID_TOURNAMENT),
    ID_PLAYER1 integer REFERENCES player (ID_PLAYER),
    ID_PLAYER2 integer REFERENCES player (ID_PLAYER),
    MATCH_RESULT integer not null,
    DATE_INCLUSION date not null

);