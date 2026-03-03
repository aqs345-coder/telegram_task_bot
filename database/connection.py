from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.task import Base

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def init_db():
    "Cria as tabelas caso não existam"
    Base.metadata.create_all(bind=engine)

def get_session():
    "Retorna uma sessão do banco de dados"
    return SessionLocal()