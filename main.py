# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Importa tudo que foi criado nos outros arquivos
# from . import models, schemas
import models
import schemas
from database import SessionLocal, engine

# Isso garante que as tabelas sejam reconhecidas pelo SQLAlchemy
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência que gerencia a sessão com o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Endpoints da API ---

@app.get("/")
def read_root():
    return {"Projeto": "API de Dados Mobilab"}

# Endpoint para ler dados da tabela SEMOB
# @app.get("/semob/", response_model=List[schemas.SemobSchema])
# def ler_dados_semob(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     dados = db.query(models.Semob).offset(skip).limit(limit).all()
#     return dados

# Endpoint para ler dados da tabela DER_VELOCIDADE
@app.get("/der/velocidade/", response_model=List[schemas.DerVelocidadeSchema])
def ler_dados_der_velocidade(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dados = db.query(models.DerVelocidade).offset(skip).limit(limit).all()
    return dados

# Endpoint para ler dados da tabela DER_FLUXO
@app.get("/der/fluxo/", response_model=List[schemas.DerFluxoSchema])
def ler_dados_der_fluxo(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dados = db.query(models.DerFluxo).offset(skip).limit(limit).all()
    return dados