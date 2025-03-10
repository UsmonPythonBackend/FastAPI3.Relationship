from pydantic import BaseModel
from typing import Optional, List, BinaryIO

class RegisterModel(BaseModel):
    id: Optional[int]
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_active: Optional[bool]
    is_staff: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            "id": 1,
            "username": "pipsudo",
            "email": "pipsudo@gmail.com",
            "password": "pipsudo123",
            "is_active": True,
            "is_staff": True

        }



#
# class ImageModel(BaseModel):
#     id: Optional[int]


class LoginModel(BaseModel):
    username: Optional[str]
    password: Optional[str]


class CargoListModel(BaseModel):
    title: Optional[str]
    quantity: Optional[int]
    transport: Optional[str]
    insurance: Optional[bool]


class CargoCreateModel(BaseModel):
    id: Optional[int]
    title: Optional[str]
    quantity: Optional[int]
    transport: Optional[str]
    insurance: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'id': 1,
            'title': 'electrocar',
            'quantity': 1,
            'transport': 'truck',
            'insurance': 'true'
        }




class ProductListModel(BaseModel):
    id: Optional[int]
    title: Optional[str]
    rating: Optional[float]
    price: Optional[float]
    color: Optional[str]


class ProductCreateModel(BaseModel):
    id: Optional[int]
    title: Optional[str]
    rating: Optional[float]
    price: Optional[float]
    color: Optional[str]


    class Config:
        orm_mode = True
        schema_extra = {
            'id': 1,
            'title': 'electrocar',
            'rating': 4.8,
            'price': 2318.31,
            'color': 'black'
        }



class OrderListModel(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    product_id: Optional[int]
    quantity: Optional[int]
    status: Optional[str]
    price: Optional[float]
    address: Optional[str]


class OrderCreateModel(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    product_id: Optional[int]
    quantity: Optional[int]
    status: Optional[str]
    price: Optional[float]
    address: Optional[str]


    class Config:
        orm_mode = True
        schema_extra = {
            'id': 1,
            'user_id': 1,
            'product_id': 1,
            'quantity': 1,
            'price': 341.31,
            'address': 'Tashkent'
        }


