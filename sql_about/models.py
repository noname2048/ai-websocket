from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)

class Data(Base):
    __tablename = "datas"

    time = Column(DateTime)
    temperature = Column
