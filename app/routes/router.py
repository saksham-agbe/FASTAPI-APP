from fastapi import APIRouter

from app.managers import *

router = APIRouter()


@router.get("/Healthcheck")
async def healthcheck():
    return await HealthcheckManager.get_health_status()

@router.get("/Libraries")
async def get_all_libraries():
    return await LibraryManager.get_all_libraries()

@router.get("/Books/{library_id}")
async def get_all_books_from_library(library_id: int):
    return await LibraryManager.get_all_books_from_library(library_id)  
