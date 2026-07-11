from sqlalchemy.orm import Session

from . import models
from . import auth


# ==========================
# Get User By Email
# ==========================

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(
        models.User.email == email
    ).first()


# ==========================
# Create New User
# ==========================

def create_user(db: Session, user):

    hashed_password = auth.hash_password(user.password)

    new_user = models.User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password,
        country=user.country,
        whatsapp=user.whatsapp,
        telegram=user.telegram,
        level=user.level,
        goal=user.goal,
        role="student"
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


# ==========================
# Authenticate User
# ==========================

def authenticate_user(db: Session, email: str, password: str):

    user = get_user_by_email(db, email)

    if not user:
        return None

    if not auth.verify_password(password, user.password):
        return None

    return user