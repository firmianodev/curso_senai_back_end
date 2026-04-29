from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship

class Base(DeclarativeBase):
    pass

class Heroi(Base):
    __tablename__ = "herois"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    classe = Column(String, nullable=False)
    nivel = Column(Integer, nullable=False)
    pontosExperiencia = Column(Integer, nullable=False)

    missoes = relationship("missao", back_populates="herois")

    def subirNivel(self):
        self.nivel +=1

    def ganharExperiencia(self):
        self.pontosExperiencia += 30
        if self.pontosExperiencia > 100:
            self.subirNivel()

    def resumo(self):
        return f"Heroi(id={self.id}, nome={self.nome!r}, classe={self.classe!r}, nivel={self.nivel!r})"

    @staticmethod
    def banco():
        return create_engine("sqlite:///herois.db", echo=False)

    @classmethod
    def criar_tabela(cls):
        Base.metadata.create_all(cls.banco())

    @classmethod
    def session(cls):
        return sessionmaker(bind=cls.banco())()