from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse
from backend.config import FRONTEND_DIR

router = APIRouter()


@router.get("/")
async def home():
    """Serve the homepage."""
    return FileResponse(FRONTEND_DIR / "index.html")


@router.get("/index.html")
async def home_redirect():
    """Redirect old .html URL to clean URL."""
    return RedirectResponse(url="/", status_code=301)


@router.get("/finance")
async def finance():
    """Serve the finance industry page."""
    return FileResponse(FRONTEND_DIR / "finance.html")


@router.get("/finance.html")
async def finance_redirect():
    return RedirectResponse(url="/finance", status_code=301)


@router.get("/insurance")
async def insurance():
    """Serve the insurance industry page."""
    return FileResponse(FRONTEND_DIR / "insurance.html")


@router.get("/insurance.html")
async def insurance_redirect():
    return RedirectResponse(url="/insurance", status_code=301)


@router.get("/hr")
async def hr():
    """Serve the HR industry page."""
    return FileResponse(FRONTEND_DIR / "hr.html")


@router.get("/hr.html")
async def hr_redirect():
    return RedirectResponse(url="/hr", status_code=301)


@router.get("/logistics")
async def logistics():
    """Serve the logistics industry page."""
    return FileResponse(FRONTEND_DIR / "logistics.html")


@router.get("/logistics.html")
async def logistics_redirect():
    return RedirectResponse(url="/logistics", status_code=301)


@router.get("/education")
async def education():
    """Serve the education industry page."""
    return FileResponse(FRONTEND_DIR / "education.html")


@router.get("/education.html")
async def education_redirect():
    return RedirectResponse(url="/education", status_code=301)


@router.get("/travel")
async def travel():
    """Serve the travel industry page."""
    return FileResponse(FRONTEND_DIR / "travel.html")


@router.get("/travel.html")
async def travel_redirect():
    return RedirectResponse(url="/travel", status_code=301)


@router.get("/privacy-policy")
async def privacy_policy():
    """Serve the privacy policy page."""
    return FileResponse(FRONTEND_DIR / "privacy-policy.html")


@router.get("/privacy-policy.html")
async def privacy_policy_redirect():
    return RedirectResponse(url="/privacy-policy", status_code=301)


@router.get("/terms-and-conditions")
async def terms_and_conditions():
    """Serve the terms and conditions page."""
    return FileResponse(FRONTEND_DIR / "terms-and-conditions.html")


@router.get("/terms-and-conditions.html")
async def terms_and_conditions_redirect():
    return RedirectResponse(url="/terms-and-conditions", status_code=301)


@router.get("/turrant-preview")
async def turrant_preview():
    """Serve the turrant preview page."""
    return FileResponse(FRONTEND_DIR / "turrant-preview.html")


@router.get("/turrant-preview.html")
async def turrant_preview_redirect():
    return RedirectResponse(url="/turrant-preview", status_code=301)
