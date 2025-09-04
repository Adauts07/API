# models.py
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class DerFluxo(Base):
    __tablename__ = "DER_FLUXO"

    # Chave primária autoincremental
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Colunas baseadas no seu arquivo 'tbl-BR-020-CVS798.xlsx - contagens.csv'
    Grupo: Mapped[str] = mapped_column(String)
    Endereco: Mapped[str] = mapped_column(String, nullable=True) # Pode ser nulo
    Intervalo: Mapped[str] = mapped_column(String)
    Data: Mapped[str] = mapped_column(String) # Usando String para acomodar o formato DD/MM/AAAA
    porte: Mapped[str] = mapped_column(String)
    fluxo: Mapped[int] = mapped_column(Integer)


class DerVelocidade(Base):
    __tablename__ = "DER_VELOCIDADE"

    # Chave primária autoincremental
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    # Colunas baseadas no seu arquivo 'tbl-DF-001-CVS144.xlsx - contagens.csv'
    Grupo: Mapped[str] = mapped_column(String)
    Endereco: Mapped[str] = mapped_column(String, nullable=True) # Pode ser nulo
    Intervalo: Mapped[str] = mapped_column(String)
    dia: Mapped[str] = mapped_column(String) # Usando String para acomodar o formato DD/MM/AAAA
    porte: Mapped[str] = mapped_column(String)
    velocidade_media: Mapped[float] = mapped_column(Float)

# Tabela SEMOB
# class Semob(Base):
#     __tablename__ = "SEMOB"
#     ... (suas colunas)