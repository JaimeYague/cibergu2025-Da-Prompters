# /app/routers/engine.py

from fastapi import APIRouter, Response
from pydantic import BaseModel
from ..engine import regex

router = APIRouter()


class MensajePayload(BaseModel):
    mensaje: str


@router.post("/replace")
async def sust(payload: MensajePayload):
    texto_original = payload.mensaje
    # return Response(content=regex.replace(mensaje), media_type="text/plain")
    resultado = regex.replace(texto_original)
    return Response(content=resultado, media_type="text/plain")
