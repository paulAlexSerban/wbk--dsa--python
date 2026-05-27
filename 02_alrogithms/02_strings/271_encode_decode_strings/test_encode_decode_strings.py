from encode_decode_strings import EncodeDecodeStrings
import pytest


@pytest.fixture
def encoder():
    return EncodeDecodeStrings()


def test_encode(encoder):
    strs = ["hello", "world"]
    encoded = encoder.encode(strs)
    assert encoded == "5#hello5#world"


def test_decode(encoder):
    s = "5#hello5#world"
    decoded = encoder.decode(s)
    assert decoded == ["hello", "world"]


def test_encode_empty(encoder):
    strs = []
    encoded = encoder.encode(strs)
    assert encoded == ""


def test_decode_empty(encoder):
    s = ""
    decoded = encoder.decode(s)
    assert decoded == []
