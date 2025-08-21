from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# String de conexão com o banco de dados Docker
DATABASE_URL = "postgresql://admin:password@db/agendadb" # "db" é o nome do serviço no docker-compose

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()