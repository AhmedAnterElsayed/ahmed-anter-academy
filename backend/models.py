from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from .database import Base


# =====================================
# Users Table
# =====================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False, index=True)

    password = Column(String(255), nullable=False)

    country = Column(String(100))

    whatsapp = Column(String(30))

    telegram = Column(String(50))

    level = Column(String(50))

    goal = Column(String(255))

    role = Column(String(20), default="student")

    created_at = Column(DateTime, default=datetime.utcnow)


# =====================================
# Courses Table
# =====================================

class Course(Base):

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)

    course_name = Column(String(100), nullable=False)

    instructor = Column(String(100), nullable=False)

    description = Column(String(500))

    level = Column(String(50))

    price = Column(Integer)

    duration = Column(String(50))

    status = Column(String(20), default="Active")

    created_at = Column(DateTime, default=datetime.utcnow)