from sqlalchemy import Column, Integer, String, Date, Text
from .database import Base

class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    evento = Column(String, index=True)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    responsavel = Column(String)
    categoria = Column(String)
    descricao = Column(Text)