from pydantic import BaseModel
from typing import Optional

class FarmCreate(BaseModel):
    user_id: int
    name: Optional[str] = None
    location: Optional[str] = None
    land_size: Optional[float] = None
    soil_type: Optional[str] = None
    crops: Optional[str] = None

class FarmOut(FarmCreate):
    id: int
    class Config:
        orm_mode = True
