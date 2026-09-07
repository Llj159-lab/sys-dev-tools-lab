import sys

import pytest

from greetlab.cli import main


def test_whitespace_name_exits_with_status_2(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["sdt-greet", "--name", "   "],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 2

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    args = parser.parse_args()

    if not args.name.strip():
        parser.error("--name must contain at least one non-whitespace character")

    print(f"Hello, {args.name}!")
