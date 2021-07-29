from typing import List, Optional

from datetime import datetime

from pydantic import BaseModel

#### RecevieData Base + CRUD ####
class ReceiveDataBase(BaseModel):
    device_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class ReceiveDataCreate(ReceiveDataBase):
    pass

class RecevieData(ReceiveDataBase):
    id: int
    is_active: bool
    warn_at_inactive: bool

    class Config:
        orm_mode = True

#### Device Base + CRUD ####
class DeviceBase(BaseModel):
    device_id : int
    name: str

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int
    device_id: int
    name: str
    receivedatas: List[RecevieData] = []

    class Config:
        orm_mode = True
