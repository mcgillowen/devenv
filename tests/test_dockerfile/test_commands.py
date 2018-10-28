"""Test the Dockerfile commands."""
import pytest

from devenv.dockerfile import commands


class TestFROM(object):
    """Test FROM command."""

    CORRECT_PARAMS = [
        pytest.param({"base_image": "test_image"}, "FROM test_image"),
        pytest.param(
            {"base_image": "test_image", "tag": "stable"}, "FROM test_image:stable"
        ),
        pytest.param(
            {"base_image": "test_image", "digest": "9a4gh"}, "FROM test_image@9a4gh"
        ),
        pytest.param(
            {"base_image": "test_image", "stage": "build"}, "FROM test_image AS build"
        ),
        pytest.param(
            {"base_image": "test_image", "tag": "stable", "stage": "build"},
            "FROM test_image:stable AS build",
        ),
        pytest.param(
            {"base_image": "test_image", "digest": "9a4gh", "stage": "build"},
            "FROM test_image@9a4gh AS build",
        ),
    ]

    @pytest.mark.parametrize("params, result", CORRECT_PARAMS)
    def test_passes_with_correct_params(self, params: dict, result: str):
        """Test that FROM doesn't fail with correct params."""
        cmd = commands.From(**params)
        assert str(cmd) == result

    def test_raises_error_with_tag_and_digest(self):
        """Test that FROM raises a RuntimeError when both tag and digest are given."""
        with pytest.raises(RuntimeError):
            commands.From(base_image="test_image", tag="stable", digest="6dae7")

    def test_raises_error_with_no_base_image(self):
        """Test that FROM raises a TypeError when no base_image is provided."""
        with pytest.raises(TypeError) as exc:
            commands.From()
        assert "__init__() missing 1 required positional argument: 'base_image'" == str(
            exc.value
        )
