from fastapi import APIRouter, HTTPException, Depends
from mysite.database.models import SubCategory
from mysite.database.schema import SubCategoryInputSchema,SubCategoryOutSchema
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List


subcategory_router = APIRouter(prefix='/subcategory' , tags=['Subcategory CRUD'])


async  def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@subcategory_router.post('/', response_model=SubCategoryOutSchema)
async def subcategory_image(user: SubCategoryInputSchema, db: Session = Depends(get_db)):
    user_db = SubCategory(**user.dict())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db



@subcategory_router.get('/', response_model=List[SubCategoryOutSchema])
async  def subcategory_image(db: Session = Depends(get_db)):
    return db.query(SubCategory).all()


@subcategory_router.get('/{subcategory_id}/', response_model=SubCategoryOutSchema)
async  def subcategory_image(subcategory_id: int, db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    return subcategory_db



@subcategory_router.put('/{subcategory_id}/', response_model=dict)
async def update_subcategory(subcategory_id: int,user: SubCategoryInputSchema,
                          db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id==subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    for subcategory_key, subcategory_value in user.dict().items():
        setattr(subcategory_db, subcategory_key, subcategory_value)

        db.commit()
        db.refresh(subcategory_db)
        return {'massage': 'катгории озгорулду'}


@subcategory_router.delete('/{subcategory}_id}/', response_model=dict)
async def subcategory_review(subcategory_id, db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id==subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    db.delete(subcategory_db)
    db.commit()
    return {'massage': 'саеитегори уда'}