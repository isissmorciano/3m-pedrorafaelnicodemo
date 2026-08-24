from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


from src.exams.recupero.es2_student import (
    analizza_codice,
    valida_codice,
    livello_codice,
    main,
)


def test_analizza_codice():
    assert analizza_codice("Abc12345") == {"maiuscole": 1, "minuscole": 2, "cifre": 5}


def test_valida_codice_valido():
    assert valida_codice("Abc12346") is True


def test_valida_codice_non_valido():
    assert valida_codice("abc12345") is False
    assert valida_codice("Abc12") is False
    assert valida_codice("Student01") is False


def test_livello_codice():
    assert livello_codice("Abc12346") == 2
    assert livello_codice("AbcdEF12345") == 3


def test_main(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "AbcdEF12345")

    main()
    captured = capsys.readouterr()

    assert "Valido (Livello 3)" in captured.out
