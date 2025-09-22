import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from the same folder
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path)

API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    raise RuntimeError("Claude API key not found. Please set ANTHROPIC_API_KEY in your environment.")

def call_claude(prompt: str, model: str = "claude-opus-4-1-20250805", max_tokens: int = 2000) -> str:
    """
    Calls Claude using the Messages API and returns text.
    """
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        content = response.json().get("content", [])
        if content and isinstance(content, list):
            return content[0].get("text", "")
        return ""
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"❌ API Error: {e}")
