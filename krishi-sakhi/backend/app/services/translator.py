import os
from app.core.config import OPENAI_API_KEY
import asyncio

# This translator tries to use OpenAI if API key is present.
# If not, it performs a simple passthrough (returns input) which still works for demo.
try:
    import openai
    if OPENAI_API_KEY:
        openai.api_key = OPENAI_API_KEY
    else:
        openai = None
except Exception:
    openai = None

async def translate_text(text: str, target_language: str = 'ml'):
    """Translate text to target_language (ISO code like 'ml' or 'en').
    If OpenAI is configured, uses it; otherwise returns a best-effort passthrough.
    """
    if openai:
        prompt = f"Translate the following text to {target_language} while keeping meaning concise:\n\n{text}"
        try:
            resp = openai.ChatCompletion.create(
                model='gpt-4o-mini' if hasattr(openai, 'ChatCompletion') else 'gpt-4o',
                messages=[{'role':'user','content':prompt}],
                max_tokens=500,
            )
            # adjust depending on API response shape
            content = resp['choices'][0]['message']['content'] if 'choices' in resp else resp['choices'][0]['text']
            return content.strip()
        except Exception as e:
            return text
    # fallback (no external API): very basic rule-based substitution for demo
    subs = {'hello':'ഹലോ','hi':'ഹായ്','yes':'അതെ','no':'ഇല്ല'}
    out = text
    for k,v in subs.items():
        out = out.replace(k, v)
    return out
