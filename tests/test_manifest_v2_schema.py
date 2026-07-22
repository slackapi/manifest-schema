import pytest
from jsonschema import ValidationError, validate

from .utils import (
    agent_view_fixture,
    get_json,
    get_schema,
    get_schema_v2,
    parametrize_agent_view_invalid,
)


# Each schema-content test runs against both:
# - the hosted router schema (what IDEs and downstream consumers fetch)
# - the local versioned schema (what the next release will ship)
# Router-specific tests like test_no_metadata stay below, outside this matrix.
SCHEMAS = [
    pytest.param(get_schema, id="hosted"),
    pytest.param(get_schema_v2, id="local"),
]

# New-feature tests only run against the local schema until the feature ships
# in a release. After release, lift them into SCHEMAS by deleting this constant.
SCHEMAS_LOCAL_ONLY = [pytest.param(get_schema_v2, id="local")]


class TestManifestV2Schema:
    @pytest.mark.parametrize("load_schema", SCHEMAS)
    def test_success(self, load_schema):
        # GIVEN
        schema = load_schema()
        manifest = get_json("tests/manifests/v2/manifest.valid.json")
        # WHEN
        try:
            validate(manifest, schema)
        except ValidationError as e:
            # THEN
            assert False, f"validation failed: {e}"

    def test_no_metadata(self):
        # GIVEN — v2 requires _metadata; router rejects when it's absent
        schema = get_schema()
        manifest = get_json("tests/manifests/v2/manifest.valid.json")
        del manifest["_metadata"]
        # WHEN
        with pytest.raises(ValidationError):
            validate(manifest, schema)
        # THEN validation exception is raised

    @pytest.mark.parametrize("load_schema", SCHEMAS)
    def test_invalid(self, load_schema):
        # GIVEN
        schema = load_schema()
        manifest = get_json("tests/manifests/v2/manifest.invalid.json")
        # WHEN
        with pytest.raises(ValidationError):
            validate(manifest, schema)
        # THEN validation exception is raised


class TestManifestV2AgentView:
    @pytest.mark.parametrize("load_schema", SCHEMAS_LOCAL_ONLY)
    def test_valid(self, load_schema):
        # GIVEN
        schema = load_schema()
        manifest = get_json("tests/manifests/v2/manifest.valid.json")
        manifest["features"]["agent_view"] = agent_view_fixture()
        # WHEN
        try:
            validate(manifest, schema)
        except ValidationError as e:
            # THEN
            assert False, f"validation failed: {e}"

    @pytest.mark.parametrize("load_schema", SCHEMAS_LOCAL_ONLY)
    @parametrize_agent_view_invalid()
    def test_invalid(self, load_schema, mutation):
        # GIVEN
        schema = load_schema()
        manifest = get_json("tests/manifests/v2/manifest.valid.json")
        manifest["features"]["agent_view"] = agent_view_fixture()
        mutation(manifest["features"]["agent_view"])
        # WHEN
        with pytest.raises(ValidationError):
            validate(manifest, schema)
        # THEN validation exception is raised
