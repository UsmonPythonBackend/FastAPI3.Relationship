from fastapi import APIRouter, status
from database import Session, ENGINE
from models import Product
from schemas import ProductListModel, ProductCreateModel
from fastapi.exceptions import HTTPException

product_router = APIRouter(prefix="/products", tags=["Products"])
session = Session(bind=ENGINE)


@product_router.get("/")
async def get_products():
    products = session.query(Product).all()
    return products



@product_router.post("/")
async def create_product(product: ProductCreateModel):
    check_id = session.query(Product).filter(Product.id == product.id).first()
    if check_id is not None:
        return {'message': 'Product id already exists'}

    new_product = Product(
        id=product.id,
        title=product.name,
        rating=product.rating,
        price=product.price,
        color=product.color
    )

    session.add(new_product)
    session.commit()

    return HTTPException(status_code=status.HTTP_200_OK, detail='Product created')


