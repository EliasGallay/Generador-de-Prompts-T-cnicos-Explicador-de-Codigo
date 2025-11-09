import os
from typing import List
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar .env
try:
    load_dotenv()
except Exception:
    pass

API_KEY = os.getenv("GEMINI_API_KEY")
USER_MODEL = os.getenv("LLM_MODEL", "").strip()

if not API_KEY:
    raise ValueError("Falta GEMINI_API_KEY en el .env")

genai.configure(api_key=API_KEY)

# Lista de candidatos en orden de preferencia
CANDIDATES: List[str] = [
    # Pro (mejor calidad)
    "gemini-1.5-pro-latest",
    "gemini-1.5-pro",
    # Flash (más barato/rápido, suele estar siempre)
    "gemini-1.5-flash-latest",
    "gemini-1.5-flash",
    # Backups
    "gemini-1.5-pro-002",
    "gemini-1.5-flash-002",
]

def _supported_models() -> List[str]:
    """Devuelve los modelos que tu clave puede usar con generateContent."""
    try:
        models = genai.list_models()
        out = []
        for m in models:
            methods = getattr(m, "supported_generation_methods", []) or []
            if "generateContent" in methods:
                # m.name suele venir como 'models/gemini-1.5-pro-latest'
                name = getattr(m, "name", "")
                if name.startswith("models/"):
                    out.append(name.split("models/")[1])
                if name:
                    out.append(name)
        seen, uniq = set(), []
        for x in out:
            if x not in seen:
                seen.add(x)
                uniq.append(x)
        return uniq
    except Exception:
        return []

def _resolve_model_name() -> str:
    # Si el usuario definió uno, usarlo primero
    order = ([USER_MODEL] if USER_MODEL else []) + CANDIDATES
    available = _supported_models()
    if available:
        for m in order:
            if not m:
                continue
            if m in available or f"models/{m}" in available:
                return m
    return order[0] if order else "gemini-1.5-flash-latest"

_MODEL_NAME = _resolve_model_name()

def _make_model(name: str):
    return genai.GenerativeModel(name)

_model = _make_model(_MODEL_NAME)

def generate_response(system: str, prompt: str) -> str:
    """
    Genera una respuesta con Gemini. Maneja 404 por nombre de modelo intentando
    again con prefijo 'models/' y luego con otros candidatos.
    """
    full_prompt = f"System:\n{system}\n\nUser:\n{prompt}"

    tried = []

    def _try(names: List[str]) -> str:
        for nm in names:
            tried.append(nm)
            try:
                resp = _make_model(nm).generate_content(full_prompt)
                return (getattr(resp, "text", "") or "").strip()
            except Exception as e:
                if not nm.startswith("models/"):
                    try_pref = f"models/{nm}"
                    tried.append(try_pref)
                    try:
                        resp = _make_model(try_pref).generate_content(full_prompt)
                        return (getattr(resp, "text", "") or "").strip()
                    except Exception:
                        pass
                continue
        raise RuntimeError(f"No se pudo invocar Gemini con los modelos probados: {tried}")

    primary = [_MODEL_NAME]
    others = [m for m in CANDIDATES if m != _MODEL_NAME]
    listed = [m for m in _supported_models() if m not in primary + others]

    return _try(primary + others + listed)
