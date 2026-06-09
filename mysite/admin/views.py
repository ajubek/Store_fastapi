from mysite.database.models import UserProfile, Category, Product, RefreshToken, SubCategory, ProductImage, Review
from sqladmin import ModelView


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.first_name, UserProfile.last_name]


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.category_name, Category.id]



class ProductAdmin(ModelView, model=Product):
    column_list = [Product.product_name,Product.product_type]


class RefreshTokenAdmin(ModelView, model=RefreshToken):
    column_list = [RefreshToken.token_user,RefreshToken.token]


class SubCategoryAdmin(ModelView, model=SubCategory):
    column_list = [SubCategory.subcategory_name, SubCategory.category_id]


class ProductImageAdmin(ModelView, model=ProductImage):
    column_list = [ProductImage.product_id,ProductImage.image]

class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.product_id,Review.product]