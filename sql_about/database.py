from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# postgres//[user]:[password]@[host](:[port])/[dbname]
SQLALCHEMY_DATABASE_URL = "postgresql://localhost:example@postgres:15001/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
