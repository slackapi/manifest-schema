import pytest
from jsonschema import ValidationError, validate

from .utils import get_json, get_local_schema, get_schema


class TestManifestV2Schema:
    def test_success(self):
        # GIVEN
        schema = get_local_schema(2)
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

    @pytest.mark.parametrize(
        "user_connections",
        [
            {"auth_hosts": ["example.com"]},
            {"is_enabled": True},
            {"is_enabled": True, "auth_hosts": []},
            {"is_enabled": True, "auth_hosts": ["https://example.com"]},
            {"is_enabled": True, "auth_hosts": ["example.com"], "auth_url": "https://example.com"},
        ],
    )
    def test_invalid_user_connections(self, user_connections):
        # GIVEN
        schema = get_local_schema(2)
        manifest = get_json("tests/manifests/v2/manifest.valid.json")
        manifest["features"]["user_connections"] = user_connections
        # WHEN
        with pytest.raises(ValidationError) as e:
            validate(manifest, schema)
        # THEN
        assert "user_connections" in e.value.absolute_path
