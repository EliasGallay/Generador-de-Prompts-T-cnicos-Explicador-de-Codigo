import json
import uuid
from datetime import datetime
from pathlib import Path

# ----------------- Configuración de paths -----------------
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
DATA_DIR.mkdir(exist_ok=True)
HISTORY_FILE = DATA_DIR / "history.json"


# ----------------- Helpers internos -----------------
def _load() -> dict:
    """Carga el historial desde JSON, o crea estructura vacía."""
    if HISTORY_FILE.exists():
        try:
            return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {"items": []}


def _save(store: dict):
    """Guarda el historial completo."""
    HISTORY_FILE.write_text(
        json.dumps(store, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


# ----------------- Funciones públicas -----------------
def add_item(kind: str, title: str, content: str, meta: dict = None):
    """Agrega un nuevo ítem al historial."""
    store = _load()
    item = {
        "id": str(uuid.uuid4()),
        "kind": kind,  # 'generator' o 'explainer'
        "title": title,
        "content": content,
        "meta": meta or {},
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    store["items"].insert(0, item)
    _save(store)
    return item


def list_items(kind: str = "all") -> list:
    """Lista ítems del historial filtrando por tipo."""
    store = _load()
    items = store.get("items", [])
    if kind == "all":
        return items
    return [it for it in items if it.get("kind") == kind]


def delete_item(item_id: str) -> bool:
    """Elimina un ítem por su ID."""
    store = _load()
    items = store.get("items", [])
    new_items = [x for x in items if x.get("id") != item_id]
    if len(new_items) == len(items):
        return False
    store["items"] = new_items
    _save(store)
    return True


def clear_items(kind: str = "all") -> int:
    """Elimina todos los ítems o solo los de cierto tipo."""
    store = _load()
    items = store.get("items", [])
    if kind == "all":
        count = len(items)
        store["items"] = []
    else:
        filtered = [x for x in items if x.get("kind") != kind]
        count = len(items) - len(filtered)
        store["items"] = filtered
    _save(store)
    return count
