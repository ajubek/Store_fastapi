from fastapi import APIRouter, HTTPException, Depends
from mysite.database.models import ProductImage
from mysite.database.schema import ProductInputImage,ProductOutImage
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List

product_image_router = APIRouter(prefix='/product_image', tags=['ProductImage CRUD'])


async  def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@product_image_router.post('/', response_model=ProductOutImage)
async def create_product_image(user: ProductInputImage, db: Session = Depends(get_db)):
    user_db = ProductImage(**user.dict())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db



@product_image_router.get('/', response_model=List[ProductOutImage])
async  def list_product_image(db: Session = Depends(get_db)):
    return db.query(ProductImage).all()


@product_image_router.get('/{product_image_id}/', response_model=ProductOutImage)
async  def detail_product_image(product_image_id: int, db: Session = Depends(get_db)):
    product_image_db = db.query(ProductImage).filter(ProductImage.id == product_image_id).first()
    if not product_image_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    return product_image_db



@product_image_router.put('/{product_image}_id}/', response_model=dict)
async def update_product_image(product_image_id: int,user: ProductInputImage,
                          db: Session = Depends(get_db)):
    product_image_db = db.query(ProductImage).filter(ProductImage.id==product_image_id).first()
    if not product_image_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    for product_image_key, product_image_value in user.dict().items():
        setattr(product_image_db, product_image_key, product_image_value)

        db.commit()
        db.refresh(product_image_db)
        return {'massage': 'катгории озгорулду'}


@product_image_router.delete('/{product_image}_id}/', response_model=dict)
async def delete_product_image(product_image_id, db: Session = Depends(get_db)):
    product_image_db = db.query(ProductImage).filter(ProductImage.id==product_image_id).first()
    if not product_image_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    db.delete(product_image_db)
    db.commit()
    return {'massage': 'саеитегори удалитл болду'}