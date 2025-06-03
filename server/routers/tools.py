# /app/routers/tools.py

from fastapi import APIRouter
from random import randint

router = APIRouter()

@router.get("/", tags=["root"])
async def read_root():
    return {"message": f"¡Hola, mundo! {randint(0, 9999)}"}
