from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship
from Models.base import Base

class Heroi(Base):
    __tablename__ = "herois"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    classe = Column(String, nullable=False)
    nivel = Column(Integer, nullable=False)
    pontosExperiencia = Column(Integer, nullable=False)

    missoes = relationship("Missao", back_populates="herois")
    
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.nivel = 1
        self.pontosExperiencia = 0

    def subirNivel(self):
        self.nivel +=1

    def ganharExperiencia(self):
        self.pontosExperiencia += 30
        if self.pontosExperiencia > 100:
            self.subirNivel()

    def resumo(self):
        return f"Heroi(id={self.id}, nome={self.nome!r}, classe={self.classe!r}, nivel={self.nivel!r})"
    