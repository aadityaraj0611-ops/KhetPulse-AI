
import pytest

from backend.app.services.farming_advice import get_farming_advice


@pytest.mark.parametrize("crop", ["wheat", "rice", "maize", "potato"])
def test_valid_crops(crop):
    result = get_farming_advice(crop)

    assert result["success"] is True
    assert result["data"]["crop"] == crop.capitalize()
    assert result["data"]["advice"]


def test_unsupported_crop():
    result = get_farming_advice("banana")

    assert result["success"] is False
    assert result["message"] == "Crop information is not available yet."


def test_crop_name_normalization():
    result = get_farming_advice(" WHEAT ")

    assert result["success"] is True
    assert result["data"]["crop"] == "Wheat"

def test_empty_crop_name():
    result = get_farming_advice("")

    assert result["success"] is False
    assert result["message"] == "Crop name cannot be empty."

def test_whitespace_crop_name():
    result = get_farming_advice(" ")

    assert result["success"] is False
    assert result["message"] == "Crop name cannot be empty."