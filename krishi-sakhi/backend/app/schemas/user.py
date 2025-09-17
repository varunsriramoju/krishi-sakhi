from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    phone: Optional[str] = None
    preferred_language: Optional[str] = 'ml'

class UserOut(BaseModel):
    id: int
    name: str
    phone: Optional[str] = None
    preferred_language: str

    class Config:
        orm_mode = True
