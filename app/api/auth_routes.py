from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth_schema import (
    RegisterRequest,
    LoginRequest
)

from app.services.auth_service import AuthService
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(payload: RegisterRequest, db: Session = Depends(get_db)):

    user = AuthService.register_user(
        db,
        payload.username,
        payload.email,
        payload.password
    )

    if not user:
        raise HTTPException(status_code=400, detail="User already exists")

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):

    token = AuthService.login_user(
        db,
        payload.email,
        payload.password
    )

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": token,
        "token_type": "bearer"
    }