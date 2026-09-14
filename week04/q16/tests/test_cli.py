import sys

import pytest

from greetlab import cli


def test_main_prints_normal_name(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "Ada"])

    cli.main()

    assert capsys.readouterr().out == "Hello, Ada!\n"


def test_main_rejects_blank_name(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   "])

    with pytest.raises(SystemExit) as excinfo:
        cli.main()

    assert excinfo.value.code == 2
    assert "--name must not be blank" in capsys.readouterr().err
