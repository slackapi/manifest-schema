import json
from typing import Callable, Dict, List, Tuple

import pytest

MANIFEST_SCHEMA_PATH = "manifest.schema.json"
MANIFEST_SCHEMA_V1_PATH = "schemas/manifest.schema.1.0.0.json"
MANIFEST_SCHEMA_V2_PATH = "schemas/manifest.schema.2.0.0.json"


def get_json(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_schema() -> Dict:
    """Top-level router schema — what IDEs and downstream consumers fetch."""
    return get_json(MANIFEST_SCHEMA_PATH)


def get_schema_v1() -> Dict:
    """Local v1 schema — what the next release artifact will ship."""
    return get_json(MANIFEST_SCHEMA_V1_PATH)


def get_schema_v2() -> Dict:
    """Local v2 schema — what the next release artifact will ship."""
    return get_json(MANIFEST_SCHEMA_V2_PATH)


# Shared agent_view block used to exercise the schema definition. Lives here so
# v1 and v2 test files stay in sync — agent_view is defined identically in both.
def agent_view_fixture() -> Dict:
    return {
        "agent_description": "A sample agent that demonstrates agent_view manifest settings.",
        "suggested_prompts": [
            {"title": "Summarize this thread", "message": "Please summarize the conversation."},
        ],
        "actions": [
            {"name": "open_settings", "description": "Open the agent settings panel."},
        ],
    }


# (id, mutation) pairs for invalid agent_view shapes — applied to a fresh fixture
# inside each test so cases stay independent. Shared between v1 and v2 because
# the constraints (maxItems, maxLength, additionalProperties: false, required
# fields) are identical across versions.
AGENT_VIEW_INVALID_CASES: List[Tuple[str, Callable[[Dict], None]]] = [
    (
        "too_many_suggested_prompts",
        lambda av: av.update(
            {"suggested_prompts": [{"title": f"p{i}", "message": f"m{i}"} for i in range(5)]}
        ),
    ),
    (
        "action_missing_description",
        lambda av: av.update({"actions": [{"name": "open_settings"}]}),
    ),
    (
        "agent_description_too_long",
        lambda av: av.update({"agent_description": "x" * 301}),
    ),
    (
        "additional_property_rejected",
        lambda av: av.update({"unexpected_field": True}),
    ),
]


def parametrize_agent_view_invalid():
    """Decorator: parametrize a test method with the shared invalid mutations."""
    return pytest.mark.parametrize(
        "mutation",
        [pytest.param(fn, id=name) for name, fn in AGENT_VIEW_INVALID_CASES],
    )
