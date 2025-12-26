from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from backend.config import FRONTEND_DIR
from backend.services.supabase import (
    get_published_posts,
    get_post_by_slug,
    get_categories,
)

router = APIRouter()


# ============== HTML Page Routes ==============

@router.get("/blog")
async def blog_listing():
    """Serve the blog listing page."""
    return FileResponse(FRONTEND_DIR / "blog.html")


@router.get("/blog.html")
async def blog_listing_redirect():
    """Redirect old .html URL to clean URL."""
    return RedirectResponse(url="/blog", status_code=301)


@router.get("/blog-post.html")
async def blog_post_redirect():
    """Redirect old .html URL to clean URL."""
    return RedirectResponse(url="/blog", status_code=301)


@router.get("/blog/{slug}")
async def blog_post(slug: str):
    """Serve the blog post page for a specific slug."""
    return FileResponse(FRONTEND_DIR / "blog-post.html")


# ============== API Routes ==============

@router.get("/api/posts")
async def api_get_posts():
    """API: Get all published posts."""
    try:
        posts = await get_published_posts()
        return JSONResponse(content={"data": posts, "error": None})
    except ValueError as e:
        # Credentials not configured
        return JSONResponse(
            status_code=503,
            content={"data": [], "error": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"data": [], "error": f"Database error: {str(e)}"}
        )


@router.get("/api/posts/{slug}")
async def api_get_post(slug: str):
    """API: Get a single post by slug."""
    try:
        post = await get_post_by_slug(slug)
        if not post:
            return JSONResponse(
                status_code=404,
                content={"data": None, "error": "Post not found"}
            )
        return JSONResponse(content={"data": post, "error": None})
    except ValueError as e:
        return JSONResponse(
            status_code=503,
            content={"data": None, "error": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"data": None, "error": f"Database error: {str(e)}"}
        )


@router.get("/api/categories")
async def api_get_categories():
    """API: Get all categories."""
    try:
        categories = await get_categories()
        return JSONResponse(content={"data": categories, "error": None})
    except ValueError as e:
        return JSONResponse(
            status_code=503,
            content={"data": [], "error": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"data": [], "error": f"Database error: {str(e)}"}
        )
