from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()


@router.get("/cv")
def cv_page(request: Request):
    return templates.TemplateResponse(
        "cv.html",
        {"request": request, "page": "cv"},
    )


@router.get("/portfolio")
def portfolio_page(request: Request):
    return templates.TemplateResponse(
        "portfolio.html",
        {"request": request, "page": "portfolio"},
    )


@router.get("/blog")
def blog_page(request: Request):
    return templates.TemplateResponse(
        "blog.html",
        {"request": request, "page": "blog"},
    )


@router.get("/contact")
def contact_page(request: Request):
    return templates.TemplateResponse(
        "contact.html",
        {"request": request, "page": "contact"},
    )
