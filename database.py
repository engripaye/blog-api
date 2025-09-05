from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite Database url
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# ENGINE
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": "false"})

# session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for models
Base = declarative_base()