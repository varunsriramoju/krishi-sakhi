from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.db.session import SessionLocal, get_db
from app.models.user import User as UserModel

router = APIRouter()

@router.post('/', response_model=UserOut)
def create_user(user_in: UserCreate, db=Depends(get_db)):
    user = UserModel(name=user_in.name, phone=user_in.phone, preferred_language=user_in.preferred_language)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get('/{user_id}', response_model=UserOut)
def get_user(user_id: int, db=Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user
