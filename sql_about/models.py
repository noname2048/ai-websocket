from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import BigInteger

from .database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(BigInteger, primary_key=True, index=True)
    device_id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)
    warn_at_inactive = Column(Boolean, default=False)

class ReceiveData(Base):
    __tablename__ = "receivedatas"

    id = Column(Integer, primary_key=True, index=True)
    device = relationship("Device", back_populates="receivedatas")
    timestamp = Column(DateTime)
    option1 = Column(String)
    option2 = Column(String)
