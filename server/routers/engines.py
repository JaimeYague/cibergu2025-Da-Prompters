# /app/routers/engine.py

from fastapi import APIRouter, Response
from random import randint
from ..engine import replace
from ..engine import regex

router = APIRouter()

@router.get("/replace/{mensaje}")
async def sust(mensaje: str):
    return Response(content=replace.replace(mensaje), media_type="text/plain")

@router.get("/regex/{mensaje}")
async def sust(mensaje: str):
    return Response(content=regex.replace(mensaje), media_type="text/plain")
