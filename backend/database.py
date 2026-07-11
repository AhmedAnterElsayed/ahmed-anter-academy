from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# =====================================
# Database Path
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "academy.db"

DATABASE_URL = f"sqlite:///{DB_PATH}"


# =====================================
# Engine
# =====================================

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# =====================================
# Session
# =====================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# =====================================
# Base
# =====================================

Base = declarative_base()


# =====================================
# Dependency
# =====================================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()