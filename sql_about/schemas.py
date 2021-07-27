from typing import List, Optional

from datetime import datetime

from pydantic import BaseModel

#### RecevieData Base + CRUD ####
class ReceiveDataBase(BaseModel):
    time: datetime

class ReceiveDataCreate(ReceiveDataBase):
    pass

class RecevieData(ReceiveDataBase):

    class Config:
        orm_mode = True

#### Device Base + CRUD ####
class DeviceBase(BaseModel):
    title: str
    description: Optional[str] = None

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int
    name: str
    receivedatas: List[RecevieData] = []

    class Config:
        orm_mode = True
