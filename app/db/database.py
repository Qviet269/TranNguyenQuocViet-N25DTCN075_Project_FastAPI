from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

localSession = sessionmaker(
    autocommit = False ,
    autoflush= False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db=localSession()
    try:
        yield db
    finally:
        db.close()