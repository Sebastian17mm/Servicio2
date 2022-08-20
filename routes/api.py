from fastapi import APIRouter
from src.endpoints import authusers

router = APIRouter()

router.include_router(authusers.router)