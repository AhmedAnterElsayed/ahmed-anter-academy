from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .database import engine
from . import models
from .routers import auth
from .routers import admin
from .routers import courses


# =====================================
# Create Database Tables
# =====================================

models.Base.metadata.create_all(bind=engine)


# =====================================
# FastAPI App
# =====================================

app = FastAPI(
    title="Ahmed Anter Academy",
    version="1.0.0"
)


# =====================================
# Static Files
# =====================================

app.mount(
    "/static",
    StaticFiles(directory="backend/static"),
    name="static"
)


# =====================================
# Templates
# =====================================

templates = Jinja2Templates(
    directory="backend/templates"
)


# =====================================
# Routers
# =====================================

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(courses.router)


# =====================================
# Home Page
# =====================================

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


# =====================================
# Register Page
# =====================================

@app.get("/register-page")
def register_page(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request
        }
    )


# =====================================
# Login Page
# =====================================

@app.get("/login-page")
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request
        }
    )


# =====================================
# Student Dashboard
# =====================================

@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request
        }
    )


# =====================================
# Admin Dashboard
# =====================================

@app.get("/admin")
def admin_page(request: Request):
    return templates.TemplateResponse(
        "admin.html",
        {
            "request": request
        }
    )


# =====================================
# Courses Page
# =====================================

@app.get("/courses-page")
def courses_page(request: Request):
    return templates.TemplateResponse(
        "courses.html",
        {
            "request": request
        }
    )