import pytest

from greetlab.name_rules import normalize_name


def test_normalize_name_strips_and_collapses_spaces():
    assert normalize_name("  Ada   Lovelace  ") == "Ada Lovelace"


def test_normalize_name_rejects_blank_name():
    with pytest.raises(ValueError, match="name must not be blank"):
        normalize_name("   ")


def test_normalize_name_rejects_digits():
    with pytest.raises(ValueError, match="name must not contain digits"):
        normalize_name("Ada2")
