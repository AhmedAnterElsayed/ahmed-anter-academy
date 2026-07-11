from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from ..database import get_db
from .. import models


router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


# ==========================
# Get all students
# ==========================

@router.get("/students")
def get_students(db: Session = Depends(get_db)):

    students = db.query(models.User).all()

    return students



# ==========================
# Data model for Add/Edit
# ==========================

class StudentUpdate(BaseModel):

    full_name: str
    email: str
    country: str
    whatsapp: str
    level: str
    goal: str



# ==========================
# Add new student
# ==========================

@router.post("/students")
def add_student(
    student: StudentUpdate,
    db: Session = Depends(get_db)
):

    new_student = models.User(

        full_name=student.full_name,
        email=student.email,
        country=student.country,
        whatsapp=student.whatsapp,
        level=student.level,
        goal=student.goal,

        # default values
        role="student",
        password="temporary"

    )


    db.add(new_student)

    db.commit()

    db.refresh(new_student)


    return new_student



# ==========================
# Edit student
# ==========================

@router.put("/students/{student_id}")
def edit_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):

    existing_student = (
        db.query(models.User)
        .filter(models.User.id == student_id)
        .first()
    )


    if not existing_student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    existing_student.full_name = student.full_name
    existing_student.email = student.email
    existing_student.country = student.country
    existing_student.whatsapp = student.whatsapp
    existing_student.level = student.level
    existing_student.goal = student.goal


    db.commit()

    db.refresh(existing_student)


    return existing_student