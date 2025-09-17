from pydantic import BaseModel
from typing import Optional, Any

class ActivityCreate(BaseModel):
    user_id: int
    farm_id: Optional[int] = None
    type: str
    payload: Optional[Any] = None

class ActivityOut(ActivityCreate):
    id: int
    class Config:
        orm_mode = True
