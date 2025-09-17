from sqlalchemy import Column, Integer, String
from app.db.base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True, unique=True)
    preferred_language = Column(String, default='ml')  # ml=en=hi etc
