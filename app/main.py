from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from .routers import pages
from .routers import blog

app = FastAPI()

# static + templates, paths from project root
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "page": "home"},
    )


app.include_router(pages.router)
app.include_router(blog.router)