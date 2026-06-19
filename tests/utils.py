import json
from typing import Dict

MANIFEST_SCHEMA_PATH = "manifest.schema.json"
MANIFEST_SCHEMA_V1_PATH = "schemas/manifest.schema.1.0.0.json"
MANIFEST_SCHEMA_V2_PATH = "schemas/manifest.schema.2.0.0.json"


def get_json(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_schema() -> Dict:
    return get_json(MANIFEST_SCHEMA_PATH)


def get_schema_v1() -> Dict:
    return get_json(MANIFEST_SCHEMA_V1_PATH)


def get_schema_v2() -> Dict:
    return get_json(MANIFEST_SCHEMA_V2_PATH)
