from sqlalchemy.orm import Session

from . import models, schemas

def get_device(db: Session, device_id: int):
    return db.query(models.Device).filter(models.Device.id == device_id).first()

def get_devices(db: Session, device: schemas.DeviceCreate, skip: int = 0, limit: int = 100):
    return db.query(models.Device).offset(skip).limit(limit).all()

def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(id=device.id)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def get_receivedatas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Device).offset(skip).limit(limit).all()

def create_receivedatas(db: Session, receivedata: schemas.ReceiveDataCreate, device_id: int):
    db_receivedata = models.ReceiveData(**receivedata.dict(), device_id=device_id)
    db.add(db_receivedata)
    db.commit()
    db.refresh(db_receivedata)
    return db_receivedata
