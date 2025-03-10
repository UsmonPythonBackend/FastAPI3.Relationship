from fastapi import APIRouter, status
from database import Session, ENGINE
from models import Cargo, Order
from http import HTTPStatus
from schemas import CargoListModel, CargoCreateModel
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi.exceptions import HTTPException







cargo_router = APIRouter(prefix="/cargo", tags=["Cargo"])
session = Session(bind=ENGINE)


@cargo_router.get("/")
async def get_cargo():
    cargo = session.query(Cargo).all()
    return cargo




@cargo_router.post("/")
async def create_cargo(cargo: CargoCreateModel):
    check_cargo = session.query(Cargo).filter(Cargo.id == cargo.id).first()
    if check_cargo is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cargo id already exists")
    check_order = session.query(Order).filter(Order.id == cargo.order_id).first()
    if check_order is None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cargo id does not exist")

    new_cargo = Cargo(
        id=cargo.id,
        title=cargo.title,
        quantity=cargo.quantity,
        transport=cargo.transport,
        insurance=cargo.insurance,
        order_id=cargo.order_id,
    )

    session.add(new_cargo)
    session.commit()

    return {"message": "Cargo created successfully", "cargo": {
        "id": new_cargo.id,
        "title": new_cargo.title,
        "quantity": new_cargo.quantity,
        "transport": new_cargo.transport,
        "insurance": new_cargo.insurance,
        "order_id": check_order.order_id,

    }}