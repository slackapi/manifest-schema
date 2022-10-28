import json
from typing import Dict

MANIFEST_SCHEMA_PATH = "manifest.schema.json"


def get_json(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_schema() -> Dict:
    return get_json(MANIFEST_SCHEMA_PATH)
