import fastapi
from mysite.api import Category, Product,SubCategory, UserProfile, Review, ProductImage, auth
import uvicorn
from mysite.admin.setup import setup_admin


shop_app = fastapi.FastAPI(title='Store Project')
shop_app.include_router(Category.category_router)
shop_app.include_router(Product.product_router)
shop_app.include_router(SubCategory.subcategory_router)
shop_app.include_router(UserProfile.userprofile_router)
shop_app.include_router(Review.review_router)
shop_app.include_router(ProductImage.product_image_router)
shop_app.include_router(auth.auth_router)
setup_admin(shop_app)

if __name__ == '__main__':
    uvicorn.run(shop_app, host= '127.0.0.1', port=8000 )