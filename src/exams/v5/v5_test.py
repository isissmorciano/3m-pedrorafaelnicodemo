from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


from src.exams.v5.v5_student import (
    analizza_numeri,
    analizza_codice,
    valida_codice,
    livello_codice,
    main,
)


def test_analizza_numeri():
    positivi_pari, count_dispari_negativi, media_assoluta = analizza_numeri(5, [2, -3, 4, -5, 6])
    assert positivi_pari == [2, 4, 6]
    assert count_dispari_negativi == 2
    assert media_assoluta == 4.0


def test_analizza_numeri_error():
    try:
        analizza_numeri(0, [])
        assert False
    except ValueError:
        assert True


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
    inputs = iter([
        "5",
        "2",
        "-3",
        "4",
        "-5",
        "6",
        "AbcdEF12345",
    ])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    main()
    captured = capsys.readouterr()

    assert "Lista inserita: [2, -3, 4, -5, 6]" in captured.out
    assert "Positivi pari: [2, 4, 6]" in captured.out
    assert "Conteggio dispari negativi: 2" in captured.out
    assert "Media assoluta: 4.0" in captured.out
    assert "Valido (Livello 3)" in captured.out
