from pydantic import BaseModel
from datetime import date
from typing import Optional


class EventoBase(BaseModel):
    evento: str
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    responsavel: Optional[str] = None
    categoria: Optional[str] = None
    descricao: Optional[str] = None


class EventoCreate(EventoBase):
    pass


class Evento(EventoBase):
    id: int

    class Config:
        orm_mode = True
