from fastapi import APIRouter, status
from database import Session, ENGINE
from models import Order, User, Product
from schemas import OrderCreateModel
from fastapi.exceptions import HTTPException


order_router = APIRouter(prefix="/orders", tags=["Orders"])
session = Session(bind=ENGINE)


@order_router.get("/")
async def get_orders():
    orders = session.query(Order).all()
    return orders


@order_router.post("/")
async def create_order(order: OrderCreateModel):
    check_order = session.query(Order).filter(Order.id == order.id).first()
    if check_order is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order id already exists")
    check_user = session.query(User).filter(User.id == order.user_id).first()
    if check_user is None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User id not exists")

    check_product = session.query(Product).filter(Product.id == order.product_id).first()
    if check_product is None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product id not exists")

    new_order = Order(
        id=order.id,
        quantity=order.quantity,
        price=order.price,
        address=order.adress,
        user_id=order.user_id,
        product_id=order.product_id,
    )

    session.add(new_order)
    session.commit()

    return {"message": "Order created successfully", "order": {
        "id": new_order.id,
        "quantity": new_order.quantity,
        "price": new_order.price,
        "address": new_order.address,
        "order_id": new_order.id,
        "product_id": new_order.product,
    }}
