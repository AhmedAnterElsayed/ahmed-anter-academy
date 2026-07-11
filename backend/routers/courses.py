from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from ..database import get_db
from .. import models


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


class CourseData(BaseModel):
    course_name: str
    instructor: str
    description: str
    level: str
    price: int
    duration: str
    status: str


# =====================================
# Get All Courses
# =====================================

@router.get("/")
def get_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()


# =====================================
# Add Course
# =====================================

@router.post("/")
def add_course(course: CourseData,
               db: Session = Depends(get_db)):

    new_course = models.Course(
        course_name=course.course_name,
        instructor=course.instructor,
        description=course.description,
        level=course.level,
        price=course.price,
        duration=course.duration,
        status=course.status
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


# =====================================
# Edit Course
# =====================================

@router.put("/{course_id}")
def edit_course(course_id: int,
                course: CourseData,
                db: Session = Depends(get_db)):

    existing = (
        db.query(models.Course)
        .filter(models.Course.id == course_id)
        .first()
    )

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    existing.course_name = course.course_name
    existing.instructor = course.instructor
    existing.description = course.description
    existing.level = course.level
    existing.price = course.price
    existing.duration = course.duration
    existing.status = course.status

    db.commit()
    db.refresh(existing)

    return existing