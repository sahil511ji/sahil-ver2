from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.config import FRONTEND_DIR
from backend.routes import pages, blog, admin

# Create FastAPI app
app = FastAPI(
    title="Turrant.ai",
    description="AI-Powered Document Collection via WhatsApp",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (images, logos, etc.)
app.mount("/images", StaticFiles(directory=FRONTEND_DIR / "images"), name="images")
app.mount("/logos", StaticFiles(directory=FRONTEND_DIR / "logos"), name="logos")
app.mount("/logos png", StaticFiles(directory=FRONTEND_DIR / "logos png"), name="logos_png")
app.mount("/logos-branded", StaticFiles(directory=FRONTEND_DIR / "logos-branded"), name="logos_branded")
app.mount("/steps", StaticFiles(directory=FRONTEND_DIR / "steps"), name="steps")
app.mount("/images_v2", StaticFiles(directory=FRONTEND_DIR / "images_v2"), name="images_v2")

# Include routers
app.include_router(pages.router)
app.include_router(blog.router)
app.include_router(admin.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=3000, reload=True)
