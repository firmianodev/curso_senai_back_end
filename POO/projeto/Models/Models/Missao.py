from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Models.base import Base

class Missao(Base):
    __tablename__ = "missao"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    recompensa_xp = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    heroi_id = Column(Integer, ForeignKey("herois.id"), nullable=False,)

    heroi = relationship("Heroi", back_populates="missoes")

    def __repr__(self):
        return f"Missao(id={self.id}, titulo={self.titulo!r}, descricao={self.descricao!r}, recompensa_xp={self.recompensa_xp!r}, status={self.status!r})"