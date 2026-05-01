from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from Models.base import Base

ENGINE = create_engine("sqlite:///herois.db", echo=False)

def criar_tabela():
    Base.metadata.create_all(ENGINE)

def session():
    Session = sessionmaker(bind=ENGINE)
    return Session()