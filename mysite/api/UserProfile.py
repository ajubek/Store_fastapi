from fastapi import APIRouter, HTTPException, Depends
from mysite.database.models import UserProfile
from mysite.database.schema import UserProfileInputSchema,UserProfileOutSchema
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List

userprofile_router = APIRouter(prefix='/user'  , tags=['Userprofile CRUD'])


async  def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#
# @userprofile_router.post('/', response_model=UserProfileOutSchema)
# async def create_user(user: UserProfileInputSchema, db: Session = Depends(get_db)):
#     user_db = UserProfile(**user.dict())
#     db.add(user_db)
#     db.commit()
#     db.refresh(user_db)
#     return user_db



@userprofile_router.get('/', response_model=List[UserProfileOutSchema])
async  def list_user(db: Session = Depends(get_db)):
    return db.query(UserProfile).all()


@userprofile_router.get('/{userprofile_id}/', response_model=UserProfileOutSchema)
async  def detail_userprofile(userprofile_id: int, db: Session = Depends(get_db)):
    userprofile_db = db.query(UserProfile).filter(UserProfile.id == userprofile_id).first()
    if not userprofile_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    return userprofile_db


@userprofile_router.put('/{userprofile_router}_id}/', response_model=dict)
async def update_userprofile(userprofile_id: int,user: UserProfileInputSchema,
                          db: Session = Depends(get_db)):
    userprofile_db = db.query(UserProfile).filter(UserProfile.id==userprofile_id).first()
    if not userprofile_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    for userprofile_key, userprofile_value in user.dict().items():
        setattr(userprofile_db, userprofile_key, userprofile_value)

        db.commit()
        db.refresh(userprofile_db)
        return {'massage': 'катгории озгорулду'}


@userprofile_router.delete('/{userprofile}_id}/', response_model=dict)
async def delete_userprofile(userprofile_id, db: Session = Depends(get_db)):
    review_db = db.query(UserProfile).filter(UserProfile.id==userprofile_id).first()
    if not review_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    db.delete(userprofile_id)
    db.commit()
    return {'massage': 'саеитегори уда'}