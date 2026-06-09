from pydantic import BaseModel, EmailStr
from typing import Optional
from .models import StatusChoices
from datetime import date, datetime

class UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username:str
    email:EmailStr
    password:str
    age:Optional[int]
    phone_number:Optional[str]




class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username:str
    email:EmailStr
    age:Optional[int]
    phone_number:Optional[str]
    status:StatusChoices
    date_registered:date

class UserLoginSchema(BaseModel):
    username:str
    password:str

class CategoryInputSchema(BaseModel):
    category_image:str
    category_name:str


class CategoryOutSchema(BaseModel):
    id:int
    category_image:str
    category_name:str




class SubCategoryInputSchema(BaseModel):
    subcategory_name:str
    category_id:int


class SubCategoryOutSchema(BaseModel):
    id:int
    subcategory_name:str
    category_id:int


class ProductInputSchema(BaseModel):
    subcategory_id:int
    product_name:str
    price:int
    article_number:int
    description:str
    product_type:bool
    video:Optional[str]
    created_date:date


class ProductOutSchema(BaseModel):
    id:int
    subcategory_id:int
    product_name:str
    price:int
    article_number:int
    description:str
    product_type:bool
    video:Optional[str]
    created_date:date



class ProductInputImage(BaseModel):
    image:str
    product_id:int



class ProductOutImage(BaseModel):
    id:int
    image:str
    product_id:int


class ReviewInputSchema(BaseModel):
    user_id: int
    product_id:int
    text:str
    stars:int


class ReviewOutSchema(BaseModel):
    id: int
    user_id: int
    product_id:int
    text:str
    stars:int
    created_date:datetime