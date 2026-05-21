from sqlalchemy.orm import Session
from app.models.user_model import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


class AuthService:

    @staticmethod
    def register_user(db: Session, username, email, password):

        existing_user = db.query(User).filter(User.email == email).first()

        if existing_user:
            return None

        new_user = User(
            username=username,
            email=email,
            hashed_password=hash_password(password)
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def login_user(db: Session, email, password):

        user = db.query(User).filter(User.email == email).first()

        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        token = create_access_token({"sub": user.email})

        return token