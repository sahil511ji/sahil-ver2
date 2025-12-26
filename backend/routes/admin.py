from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from pydantic import BaseModel
from typing import Optional, List
from backend.config import FRONTEND_DIR
from backend.services.supabase import (
    get_all_posts,
    create_post,
    update_post,
    delete_post,
)

router = APIRouter()


# ============== Pydantic Models ==============

class PostCreate(BaseModel):
    title: str
    slug: str
    excerpt: Optional[str] = None
    content: Optional[str] = None
    featured_image: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    author: Optional[str] = "Turrant Team"
    card_color: Optional[str] = "teal"
    published: Optional[bool] = False
    featured: Optional[bool] = False
    meta_title: Optional[str] = None
    meta_description: Optional[str] = None


class PostUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    excerpt: Optional[str] = None
    content: Optional[str] = None
    featured_image: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    author: Optional[str] = None
    card_color: Optional[str] = None
    published: Optional[bool] = None
    featured: Optional[bool] = None
    meta_title: Optional[str] = None
    meta_description: Optional[str] = None


# ============== HTML Page Routes ==============

@router.get("/admin")
async def admin_dashboard():
    """Serve the admin dashboard page."""
    return FileResponse(FRONTEND_DIR / "blog-admin.html")


@router.get("/blog-admin.html")
async def admin_redirect():
    """Redirect old .html URL to clean URL."""
    return RedirectResponse(url="/admin", status_code=301)


@router.get("/blog-admin")
async def blog_admin_redirect():
    """Redirect /blog-admin to /admin."""
    return RedirectResponse(url="/admin", status_code=301)


# ============== API Routes ==============

@router.get("/api/admin/posts")
async def api_get_all_posts():
    """API: Get all posts (including drafts) for admin."""
    try:
        posts = await get_all_posts()
        return JSONResponse(content={"data": posts})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api/admin/posts")
async def api_create_post(post: PostCreate):
    """API: Create a new blog post."""
    try:
        post_data = post.model_dump(exclude_none=True)
        result = await create_post(post_data)
        return JSONResponse(content={"data": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/api/admin/posts/{post_id}")
async def api_update_post(post_id: str, post: PostUpdate):
    """API: Update an existing blog post."""
    try:
        post_data = post.model_dump(exclude_none=True)
        result = await update_post(post_id, post_data)
        return JSONResponse(content={"data": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/api/admin/posts/{post_id}")
async def api_delete_post(post_id: str):
    """API: Delete a blog post."""
    try:
        result = await delete_post(post_id)
        return JSONResponse(content={"data": result, "message": "Post deleted"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
