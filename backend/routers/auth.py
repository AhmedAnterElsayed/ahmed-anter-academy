from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import schemas
from .. import crud
from .. import auth

router = APIRouter(tags=["Authentication"])


@router.post("/register")
def register(user: schemas.UserRegister, db: Session = Depends(get_db)):

    existing_user = crud.get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    new_user = crud.create_user(db, user)

    return {
        "message": "Registration successful!",
        "user_id": new_user.id
    }


@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):

    db_user = crud.authenticate_user(
        db,
        user.email,
        user.password
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    token = auth.create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "full_name": db_user.full_name,
        "role": db_user.role
    }