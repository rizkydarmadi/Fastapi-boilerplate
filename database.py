from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import (
    DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, 
    DATABASE_NAME, DATABASE_PORT
)

# Create sqlalchemy session
username = DATABASE_USER
password = DATABASE_PASSWORD
host = DATABASE_HOST
port = DATABASE_PORT
database = DATABASE_NAME

engine = create_engine(
        f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
        , pool_size=20, max_overflow=0, pool_timeout=300
    )

Session = sessionmaker(engine, future=True)
Base = declarative_base()

# for alembic automigrations
from app.user.model import User