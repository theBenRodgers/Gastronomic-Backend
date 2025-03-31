from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin

from app.config import get_settings
from app.routers.ingredients import router as ingredients_router
from app.routers.recipes import router as recipes_router

app = FastAPI()

# Include routers
app.include_router(ingredients_router)
app.include_router(recipes_router)

settings = get_settings()
origins = [settings.frontend_url]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    firebase_admin.initialize_app()
