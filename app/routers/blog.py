import os
import frontmatter
import markdown
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

POSTS_DIR = Path("app/static/content/posts")


def load_posts():
    posts = []
    for file in POSTS_DIR.glob("*.md"):
        post_data = frontmatter.load(file)

        html_body = markdown.markdown(
            post_data.content,
            extensions=["fenced_code", "tables", "toc", "footnotes"]
        )

        posts.append({
            "title": post_data["title"],
            "date": post_data["date"],
            "category": post_data.get("category", "ideas-and-reflections"),
            "tags": post_data.get("tags", []),
            "slug": post_data.get("slug") or file.stem,
            "excerpt": post_data.get("excerpt") or post_data.content[:180] + "...",
            "html": html_body,
        })

    # sort newest first
    return sorted(posts, key=lambda x: x["date"], reverse=True)


POSTS = load_posts()


@router.get("/blog")
def blog_index(request: Request):
    return templates.TemplateResponse(
        "blog.html",
        {"request": request, "posts": POSTS}
    )


@router.get("/blog/{slug}")
def blog_post(request: Request, slug: str):
    post = next((p for p in POSTS if p["slug"] == slug), None)
    if not post:
        return templates.TemplateResponse("blog_not_found.html", {"request": request}, status_code=404)

    return templates.TemplateResponse(
        "post.html",
        {"request": request, "post": post}
    )
