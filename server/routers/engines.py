# /app/routers/engine.py

from fastapi import APIRouter
from random import randint
from ..engine import replace

router = APIRouter()

@router.get("/", tags=["root"])
async def read_root():
    return {"message": f"¡Hola, mundo! {randint(0, 9999)}"}

@router.get("/replace/{mensaje}")
async def sust(mensaje: str):
    return replace.replace(mensaje)
