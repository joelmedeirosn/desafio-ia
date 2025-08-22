from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine
from typing import Optional


models.Base.metadata.create_all(bind=engine)  # cria a tabela se não existir

app = FastAPI()


# função para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/eventos/", response_model=schemas.Evento)
def create_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):

    db_evento = models.Evento(**evento.dict())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento


@app.get("/eventos/", response_model=list[schemas.Evento])
def read_eventos(
    skip: int = 0,
    limit: int = 100,
    evento: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(models.Evento)
    if evento:
        # Filtra pelo nome do evento (busca parcial e sem diferenciar maiúsculas/minúsculas)
        query = query.filter(models.Evento.evento.ilike(f"%{evento}%"))

    eventos = query.offset(skip).limit(limit).all()
    return eventos

@app.put("/eventos/{evento_id}", response_model=schemas.Evento)
def update_evento(evento_id: int, evento_update: schemas.EventoCreate, db: Session = Depends(get_db)):
    db_evento = db.query(models.Evento).filter(models.Evento.id == evento_id).first()
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    
    for var, value in vars(evento_update).items():
        if value is not None:
            setattr(db_evento, var, value)
            
    db.commit()
    db.refresh(db_evento)
    return db_evento

@app.delete("/eventos/{evento_id}", status_code=204)
def delete_evento(evento_id: int, db: Session = Depends(get_db)):
    db_evento = db.query(models.Evento).filter(models.Evento.id == evento_id).first()
    if db_evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
        
    db.delete(db_evento)
    db.commit()
    return {"ok": True} # retorna um 204 No Content por padrão
