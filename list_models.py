"""Prints the model names your API key can use.
Run from the project folder:  python list_models.py
"""
import tomllib

from openai import OpenAI

SKIP_WORDS = ("whisper", "tts", "guard", "orpheus", "playai", "embed")  # not text chat models

with open(".streamlit/secrets.toml", "rb") as f:
    secrets = tomllib.load(f)

client = OpenAI(
    api_key=secrets["LLM_API_KEY"],
    base_url=secrets.get("LLM_BASE_URL", "https://api.groq.com/openai/v1"),
)

for model in sorted(client.models.list().data, key=lambda m: m.id):
    if not any(word in model.id.lower() for word in SKIP_WORDS):
        print(model.id)
