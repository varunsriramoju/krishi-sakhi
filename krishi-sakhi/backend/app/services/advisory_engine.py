import asyncio
from typing import Dict, Any
from .translator import translate_text

# Simple rule based advisory engine for demo
async def generate_advisory(user, farm, activity_text: str, target_language='ml'):
    # Normalize input (we assume english for logic; real app should translate to en first)
    text = activity_text.lower()
    advice = "Here is a general tip: follow crop calendar and watch weather."
    if 'pest' in text or 'പേസ്റ്റ്' in text or 'pest' in activity_text:
        advice = "Possible pest issue reported. Inspect leaves; consider safe pesticide or consult agronomist."
    if 'fertil' in text or 'വള' in text:
        advice = "Avoid fertiliser before heavy rain; apply in the morning on dry days."
    # translate to target language if needed
    translated = await translate_text(advice, target_language=target_language)
    return {'advisory':translated, 'raw':advice}
