"""Tests for config.references"""

import pytest

import deepr as dpr


@pytest.mark.parametrize(
    "item, references, expected",
    [
        (None, None, None),
        ("@reference", {"@reference": "value"}, "value"),
        ("@reference", None, ValueError),
        (["@reference"], {"@reference": "value"}, ["value"]),
        (("@reference",), {"@reference": "value"}, ("value",)),
        ({"key": "@reference"}, {"@reference": "value"}, {"key": "value"}),
    ],
)
def test_config_fill_refs(item, references, expected):
    """Test fill_refs"""
    if expected is ValueError:
        with pytest.raises(ValueError):
            dpr.config.fill_references(item, references)
    else:
        assert dpr.config.fill_references(item, references) == expected
