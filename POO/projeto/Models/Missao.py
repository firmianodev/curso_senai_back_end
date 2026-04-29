from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship

class Base(DeclarativeBase):
    pass

class Missao(Base):
    __tablename__ = "missao"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    recompensaXp = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    heroi_id = Column(Integer, ForeignKey("heroi_id"), nullable=False,)

    herois = relationship("heroi", back_populates="missoes")

    def __repr__(self):
        return f"Missao(id={self.id}, titulo={self.titulo!r}, descricao={self.descricao!r}, recompensaXp={self.recompensaXp!r}, status={self.status!r})"

    @staticmethod
    def banco():
        return create_engine("sqlite:///missoes.db", echo=False)

    @classmethod
    def criar_tabela(cls):
        Base.metadata.create_all(cls.banco())

    @classmethod
    def session(cls):
        return sessionmaker(bind=cls.banco())()