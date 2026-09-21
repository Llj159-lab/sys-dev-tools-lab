import pytest

from greetlab.name_rules import normalize_name


def test_normalize_name_returns_normal_name():
    assert normalize_name("Alice Smith") == "Alice Smith"


def test_normalize_name_rejects_blank_name():
    with pytest.raises(ValueError, match="must not be blank"):
        normalize_name("   ")
