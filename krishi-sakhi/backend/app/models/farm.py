from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base

class Farm(Base):
    __tablename__ = 'farms'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String, nullable=True)
    location = Column(String, nullable=True)  # simple address or geojson text
    land_size = Column(Float, nullable=True)
    soil_type = Column(String, nullable=True)
    crops = Column(String, nullable=True)  # comma separated for starter
