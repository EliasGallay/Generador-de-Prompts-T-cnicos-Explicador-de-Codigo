# app/utils/storage.py
from __future__ import annotations
import json
from datetime import datetime
from pathlib import Path
from typing import Literal, TypedDict, Optional

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)
HIST_FILE = DATA_DIR / "history.json"

class Item(TypedDict):
    id: str
    kind: Literal["generator","explainer"]
    title: str
    content: str
    meta: dict
    created_at: str

def _load() -> list[Item]:
    if not HIST_FILE.exists():
        return []
    try:
        return json.loads(HIST_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []

def _save(items: list[Item]) -> None:
    HIST_FILE.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")

def add_item(kind: Literal["generator","explainer"], title: str, content: str, meta: Optional[dict]=None) -> Item:
    items = _load()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_item: Item = {
        "id": f"{int(datetime.now().timestamp()*1000)}",
        "kind": kind,
        "title": title.strip() or ("Prompt" if kind=="generator" else "Explicación"),
        "content": content,
        "meta": meta or {},
        "created_at": now,
    }
    items.insert(0, new_item)
    _save(items)
    return new_item

def list_items(kind: Literal["generator","explainer","all"]="all", limit: int=100) -> list[Item]:
    items = _load()
    if kind != "all":
        items = [i for i in items if i["kind"] == kind]
    return items[:limit]

def get_item(item_id: str) -> Optional[Item]:
    for i in _load():
        if i["id"] == item_id:
            return i
    return None
