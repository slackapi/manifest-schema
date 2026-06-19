import pytest
from jsonschema import ValidationError, validate

from .utils import get_json, get_schema


class TestManifestV1Schema:
    def test_success(self):
        # GIVEN
        schema = get_schema()
        manifest = get_json("tests/manifests/v1/manifest.valid.json")
        # WHEN
        try:
            validate(manifest, schema)
        except ValidationError as e:
            # THEN
            assert False, f"validation failed: {e}"

    def test_no_metadata(self):
        # GIVEN
        schema = get_schema()
        manifest = get_json("tests/manifests/v1/manifest.valid.json")
        del manifest["_metadata"]
        # WHEN
        try:
            validate(manifest, schema)
        except ValidationError as e:
            # THEN
            assert False, f"validation failed: {e}"

    def test_invalid(self):
        # GIVEN
        schema = get_schema()
        manifest = get_json("tests/manifests/v1/manifest.invalid.json")
        # WHEN
        with pytest.raises(ValidationError):
            validate(manifest, schema)
        # THEN validation exception is raised
