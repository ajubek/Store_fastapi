from fastapi import APIRouter, HTTPException, Depends
from mysite.database.models import Category
from mysite.database.schema import CategoryInputSchema,CategoryOutSchema
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List

category_router = APIRouter(prefix='/category', tags=['Category CRUD'])


async  def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@category_router.post('/', response_model=CategoryOutSchema)
async def create_category(user: CategoryInputSchema, db: Session = Depends(get_db)):
    user_db = Category(**user.dict())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db



@category_router.get('/', response_model=List[CategoryOutSchema])
async  def list_category(db: Session = Depends(get_db)):
    return db.query(Category).all()


@category_router.get('/{category_id}/', response_model=CategoryOutSchema)
async  def detail_category(category_id: int, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    return category_db


@category_router.put('/{category_id}/', response_model=dict)
async def update_category(category_id: int ,user: CategoryInputSchema,
                          db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id==category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    for category_key, category_value in user.dict().items():
        setattr(category_db, category_key, category_value)

        db.commit()
        db.refresh(category_db)
        return {'massage': 'катгории озгорулду'}


@category_router.delete('/{category_id}/', response_model=dict)
async def delete_category(category_id, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id==category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    db.delete(category_db)
    db.commit()
    return {'massage': 'саеитегори удалитл болду'}
