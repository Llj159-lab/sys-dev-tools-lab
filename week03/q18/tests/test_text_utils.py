from text_utils import normalize_spaces


def test_normal_text():
    assert normalize_spaces("hello world") == "hello world"


def test_multiple_spaces():
    assert normalize_spaces("hello   world") == "hello world"


def test_tabs_and_newlines():
    assert normalize_spaces("hello\t\nworld") == "hello world"


def test_empty_text():
    assert normalize_spaces("") == ""
