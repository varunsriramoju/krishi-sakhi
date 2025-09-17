from fastapi import APIRouter, Body
from app.services.advisory_engine import generate_advisory
from app.services.translator import translate_text
import asyncio

router = APIRouter()

@router.post('/generate')
async def advisory_endpoint(payload: dict = Body(...)):
    # payload: { 'user': {...}, 'farm': {...}, 'text': '...' , 'language': 'ml' }
    user = payload.get('user', {})
    farm = payload.get('farm', {})
    text = payload.get('text', '')
    lang = payload.get('language', 'ml')
    res = await generate_advisory(user, farm, text, target_language=lang)
    return res
