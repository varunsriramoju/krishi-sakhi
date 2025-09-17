from fastapi import APIRouter, Depends, HTTPException
from app.schemas.activity import ActivityCreate, ActivityOut
from app.db.session import get_db
from app.models.activity import Activity as ActivityModel

router = APIRouter()

@router.post('/', response_model=ActivityOut)
def log_activity(a: ActivityCreate, db=Depends(get_db)):
    act = ActivityModel(**a.dict())
    db.add(act)
    db.commit()
    db.refresh(act)
    return act

@router.get('/user/{user_id}')
def list_activities(user_id: int, db=Depends(get_db)):
    acts = db.query(ActivityModel).filter(ActivityModel.user_id==user_id).order_by(ActivityModel.created_at.desc()).all()
    return acts
