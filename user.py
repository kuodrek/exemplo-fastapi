import models, schemas as sch, utils
from fastapi import Response, status, HTTPException, Depends, APIRouter
from database import get_db
from sqlalchemy.orm import Session
from typing import Optional, List  

router = APIRouter(prefix='/users', tags=['Users'])

# ENDPOINTS DE USUÁRIO
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=sch.UserOut) 
def create_user(user: sch.UserCreate, db: Session = Depends(get_db)):
    # hash user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", response_model=sch.UserOut) # id: path parameter
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    return user