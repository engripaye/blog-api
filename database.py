from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite Database url
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

