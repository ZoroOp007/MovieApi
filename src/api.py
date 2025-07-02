from fastapi import APIRouter

from .Auth.views import router as auth_router
from .Movie.views import router as movie_router

router = APIRouter(prefix="/v1")

router.include_router(auth_router)
router.include_router(movie_router)