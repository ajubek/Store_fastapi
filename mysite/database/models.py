from .db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, Date, ForeignKey, Text, Boolean, DateTime
from enum import Enum as PyEnum
from datetime import date, datetime
from typing import List


class StatusChoices(str, PyEnum):
    gold = 'gold'
    silver = 'silver'
    bronze = 'bronze'
    simple = 'simple'


class UserProfile(Base):
    __tablename__ = 'profile'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    age: Mapped[int | None] = mapped_column(Integer, nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String, nullable=True)
    status: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), default=StatusChoices.simple)
    date_registered: Mapped[date] = mapped_column(Date, default=date.today)

    users_review: Mapped[List['Review']] = relationship(back_populates='user', cascade='all, delete-orphan')
    user_token: Mapped[List['RefreshToken']] = relationship(back_populates='token_user')



class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_image: Mapped[str] = mapped_column(String)
    category_name: Mapped[str] = mapped_column(String(20), unique=True)

    subcategories: Mapped[List['SubCategory']] = relationship(back_populates='category', cascade='all, delete-orphan')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    profile_id: Mapped[int] = mapped_column(Integer, ForeignKey('profile.id'))
    token_user: Mapped[UserProfile] = relationship(UserProfile, back_populates='user_token')
    token: Mapped[str] = mapped_column(String)
    created_date:Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())




class SubCategory(Base):
    __tablename__ = 'subcategory'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subcategory_name: Mapped[str] = mapped_column(String(50))
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))

    category: Mapped[Category] = relationship(back_populates='subcategories')
    products: Mapped[List['Product']] = relationship(back_populates='subcategory', cascade='all, delete-orphan')

    def __str__(self):
        return f'{self.subcategory_name}, {self.category}'


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey('subcategory.id'))
    product_name: Mapped[str] = mapped_column(String(50))
    price: Mapped[int] = mapped_column(Integer)
    article_number: Mapped[int] = mapped_column(Integer, unique=True)
    description: Mapped[str] = mapped_column(Text)
    product_type: Mapped[bool] = mapped_column(Boolean)
    video: Mapped[str | None] = mapped_column(String, nullable=True)
    created_date: Mapped[date] = mapped_column(Date, default=date.today)

    subcategory: Mapped[SubCategory] = relationship(back_populates='products')
    images: Mapped[List['ProductImage']] = relationship(back_populates='product', cascade='all, delete-orphan')
    reviews: Mapped[List['Review']] = relationship(back_populates='product', cascade='all, delete-orphan')


class ProductImage(Base):
    __tablename__ = 'product_image'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image: Mapped[str] = mapped_column(String)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))

    product: Mapped[Product] = relationship(back_populates='images')


class Review(Base):
    __tablename__ = 'review'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    user: Mapped[UserProfile] = relationship(back_populates='users_review')
    text: Mapped[str] = mapped_column(Text)
    stars: Mapped[int] = mapped_column(Integer)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    product: Mapped[Product] = relationship(back_populates='reviews')
