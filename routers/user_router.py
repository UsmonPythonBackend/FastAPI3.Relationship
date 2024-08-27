from fastapi import APIRouter, status
from http import HTTPStatus
from schemas import RegisterModel, LoginModel
from database import Session, ENGINE
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi.exceptions import HTTPException


user_router = APIRouter(prefix="/user", tags=["user"])
session = Session(bind=ENGINE)


@user_router.get("/")
async def auth():
    return {"message": "Auth page"}


@user_router.get("/login")
async def login():
    return {"message": "Login page"}


@user_router.post("/login")
async def user_login(user: LoginModel):
    check_user = session.query(User).filter(User.username == user.username).first()
    if check_user is not None:
        if check_password_hash(check_user.password, user.password):
            return HTTPException(status_code=status.HTTP_200_OK, detail="Login successful")

        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@user_router.get("/register")
async def get_register():
    return {"message": "Register page"}


@user_router.post("/register", status_code=HTTPStatus.CREATED)
async def create_user(user: RegisterModel):
    check_username = session.query(User).filter(User.username == user.username).first()
    if check_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")


    check_email = session.query(User).filter(User.email == user.email).first()
    if check_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")



    new_user = User(
        id=user.id,
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff
    )

    session.add(new_user)
    session.commit()
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="User created successfully")



@user_router.get("/users")
async def get_users():
    users = session.query(User).all()
    return users
