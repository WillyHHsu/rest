# rest
an rest API example

## Gerenciamento de pacotes com poetry
poetry install

## Docker

Use o docker-compose para rodar o **db**, **adminer** e  **app**, a aplicação, em containers

```sh
docker-compose up -d [db, adminer, app]
```

> `-d` Detached mode: Run containers in the background

A aplicação depende de **db** e com `docker-compose up -d app` dois containers serão executados db e app

A aplicação **db** executa os sql's em `./tables/init/` quando for iniciada pela primeira vez, persiste os dados em um volume, para apagar os dados do db execute: `docker-compose down -v`

> `-v` Remove data volumes
`docker-compose up db` 

## Endpoints

### Criação
Na pasta db estão os modelos para uso com o banco de dados e ORM
Na pasta schemas estão os modelos que serão usados ao receber ou retornar dados

```py
@app.post("/tournament",
          summary='Cadastra um novo torneio',
          response_model=schemas.models.Tournament)  # Modelo usado para documentação da resposta
def new_tournament(tornament_request: schemas.models.Tournament): # Modelo usado para cadastro no database
    db.session.add(db.models.Tornament(tornament_request))
    db.session.commit() # Modelo sendo retornando na resolução requisição
    return schemas.models.Tournament(**tornament_request)
```

## DOC

http://localhost:8000/docs/

http://localhost:8000/redoc/
