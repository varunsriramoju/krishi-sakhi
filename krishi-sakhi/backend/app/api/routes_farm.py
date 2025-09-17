from fastapi import APIRouter, Depends, HTTPException
from app.schemas.farm import FarmCreate, FarmOut
from app.db.session import get_db
from app.models.farm import Farm as FarmModel

router = APIRouter()

@router.post('/', response_model=FarmOut)
def create_farm(farm_in: FarmCreate, db=Depends(get_db)):
    farm = FarmModel(**farm_in.dict())
    db.add(farm)
    db.commit()
    db.refresh(farm)
    return farm

@router.get('/{farm_id}', response_model=FarmOut)
def get_farm(farm_id: int, db=Depends(get_db)):
    farm = db.query(FarmModel).filter(FarmModel.id==farm_id).first()
    if not farm:
        raise HTTPException(status_code=404, detail='Farm not found')
    return farm
