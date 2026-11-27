import json
from typing import Dict

MANIFEST_SCHEMA_PATH = "manifest.schema.json"

LOCAL_SCHEMA_PATHS = {
    1: "schemas/manifest.schema.1.0.0.json",
    2: "schemas/manifest.schema.2.0.0.json",
}


def get_json(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_schema() -> Dict:
    return get_json(MANIFEST_SCHEMA_PATH)


def get_local_schema(major_version: int) -> Dict:
    return get_json(LOCAL_SCHEMA_PATHS[major_version])
