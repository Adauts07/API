# schemas.py
from pydantic import BaseModel
from typing import Optional # Usado para campos que podem ser nulos

# Schema para a tabela DER_FLUXO
class DerFluxoSchema(BaseModel):
    id: int
    Grupo: str
    Endereco: Optional[str] = None # Define que o campo é opcional
    Intervalo: str
    Data: str
    porte: str
    fluxo: int

    class Config:
        orm_mode = True # Permite que o Pydantic leia o objeto do SQLAlchemy

# Schema para a tabela DER_VELOCIDADE
class DerVelocidadeSchema(BaseModel):
    id: int
    Grupo: str
    Endereco: Optional[str] = None # Define que o campo é opcional
    Intervalo: str
    dia: str
    porte: str
    velocidade_media: float

    class Config:
        orm_mode = True

# Tabela SEMOB
# class SemobSchema(BaseModel):
#     ... (seus campos)