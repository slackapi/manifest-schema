import pytest
from jsonschema import ValidationError, validate

from .utils import get_json, get_schema, get_schema_v2


class TestManifestV2Schema:
    def test_success(self):
        # GIVEN
        schema = get_schema()
        manifest = get_json("tests/manifests/v2/manifest.valid.json")
        # WHEN
        try:
            validate(manifest, schema)
        except ValidationError as e:
            # THEN
            assert False, f"validation failed: {e}"

    def test_no_metadata(self):
        # GIVEN
        schema = get_schema()
        manifest = get_json("tests/manifests/v2/manifest.valid.json")
        del manifest["_metadata"]
        # WHEN
        with pytest.raises(ValidationError):
            validate(manifest, schema)
        # THEN validation exception is raised

    def test_invalid(self):
        # GIVEN
        schema = get_schema()
        manifest = get_json("tests/manifests/v2/manifest.invalid.json")
        # WHEN
        with pytest.raises(ValidationError):
            validate(manifest, schema)
        # THEN validation exception is raised


def _agent_view_fixture():
    return {
        "agent_description": "A sample agent that demonstrates agent_view manifest settings.",
        "suggested_prompts": [
            {
                "title": "Summarize this thread",
                "message": "Please summarize the conversation in this thread.",
            },
        ],
        "actions": [
            {"name": "open_settings", "description": "Open the agent settings panel."},
        ],
    }


class TestManifestV2AgentView:
    """Validates the local v2 schema (not the GitHub-pinned router) so changes
    to schemas/manifest.schema.2.0.0.json are exercised before release."""

    def _manifest_with_agent_view(self):
        manifest = get_json("tests/manifests/v2/manifest.valid.json")
        manifest["features"]["agent_view"] = _agent_view_fixture()
        return manifest

    def test_agent_view_valid(self):
        # GIVEN — manifest with a fully populated agent_view block
        schema = get_schema_v2()
        manifest = self._manifest_with_agent_view()
        # WHEN
        try:
            validate(manifest, schema)
        except ValidationError as e:
            # THEN
            assert False, f"validation failed: {e}"

    def test_agent_view_too_many_prompts(self):
        # GIVEN — suggested_prompts is capped at 4
        schema = get_schema_v2()
        manifest = self._manifest_with_agent_view()
        manifest["features"]["agent_view"]["suggested_prompts"] = [
            {"title": f"prompt {i}", "message": f"message {i}"} for i in range(5)
        ]
        # WHEN
        with pytest.raises(ValidationError):
            validate(manifest, schema)
        # THEN validation exception is raised

    def test_agent_view_action_missing_description(self):
        # GIVEN — actions[].description is required
        schema = get_schema_v2()
        manifest = self._manifest_with_agent_view()
        manifest["features"]["agent_view"]["actions"] = [{"name": "open_settings"}]
        # WHEN
        with pytest.raises(ValidationError):
            validate(manifest, schema)
        # THEN validation exception is raised

    def test_agent_view_description_too_long(self):
        # GIVEN — agent_description is capped at 300 chars
        schema = get_schema_v2()
        manifest = self._manifest_with_agent_view()
        manifest["features"]["agent_view"]["agent_description"] = "x" * 301
        # WHEN
        with pytest.raises(ValidationError):
            validate(manifest, schema)
        # THEN validation exception is raised

    def test_agent_view_additional_property_rejected(self):
        # GIVEN — additionalProperties is false on agent_view
        schema = get_schema_v2()
        manifest = self._manifest_with_agent_view()
        manifest["features"]["agent_view"]["unexpected_field"] = True
        # WHEN
        with pytest.raises(ValidationError):
            validate(manifest, schema)
        # THEN validation exception is raised
