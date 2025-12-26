from typing import Optional, List, Dict, Any
from backend.config import SUPABASE_URL, SUPABASE_ANON_KEY

# Lazy-loaded Supabase client
_supabase_client = None


def get_supabase_client():
    """Get or create Supabase client. Raises error if credentials are missing."""
    global _supabase_client

    if _supabase_client is not None:
        return _supabase_client

    # Check for valid credentials
    if not SUPABASE_URL or SUPABASE_URL == "https://your-project-id.supabase.co":
        raise ValueError("SUPABASE_URL not configured. Please update .env file.")

    if not SUPABASE_ANON_KEY or SUPABASE_ANON_KEY == "your-anon-key-here":
        raise ValueError("SUPABASE_ANON_KEY not configured. Please update .env file.")

    from supabase import create_client, Client
    _supabase_client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    return _supabase_client


async def get_published_posts() -> List[Dict[str, Any]]:
    """Get all published blog posts, ordered by published date."""
    client = get_supabase_client()
    response = client.table("blog_posts") \
        .select("*") \
        .eq("published", True) \
        .order("published_at", desc=True) \
        .execute()
    return response.data or []


async def get_post_by_slug(slug: str) -> Optional[Dict[str, Any]]:
    """Get a single published post by its slug."""
    client = get_supabase_client()
    response = client.table("blog_posts") \
        .select("*") \
        .eq("slug", slug) \
        .eq("published", True) \
        .maybe_single() \
        .execute()
    return response.data


async def get_all_posts() -> List[Dict[str, Any]]:
    """Get all blog posts (including drafts) for admin."""
    client = get_supabase_client()
    response = client.table("blog_posts") \
        .select("*") \
        .order("created_at", desc=True) \
        .execute()
    return response.data or []


async def get_categories() -> List[Dict[str, Any]]:
    """Get all blog categories."""
    client = get_supabase_client()
    response = client.table("blog_categories") \
        .select("*") \
        .order("name") \
        .execute()
    return response.data or []


async def create_post(post_data: dict) -> Dict[str, Any]:
    """Create a new blog post."""
    client = get_supabase_client()
    response = client.table("blog_posts") \
        .insert(post_data) \
        .execute()
    return response.data[0] if response.data else {}


async def update_post(post_id: str, post_data: dict) -> Dict[str, Any]:
    """Update an existing blog post."""
    client = get_supabase_client()
    response = client.table("blog_posts") \
        .update(post_data) \
        .eq("id", post_id) \
        .execute()
    return response.data[0] if response.data else {}


async def delete_post(post_id: str) -> bool:
    """Delete a blog post."""
    client = get_supabase_client()
    response = client.table("blog_posts") \
        .delete() \
        .eq("id", post_id) \
        .execute()
    return True
