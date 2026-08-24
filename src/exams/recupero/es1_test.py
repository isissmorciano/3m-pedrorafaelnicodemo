from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


from src.exams.recupero.es1_student import analizza_numeri, main


def test_analizza_numeri():
    positivi_pari, dispari_negativi, media_assoluta = analizza_numeri(5, [2, -3, 4, -5, 6])
    assert positivi_pari == [2, 4, 6]
    assert dispari_negativi == 2
    assert media_assoluta == 4.0


def test_analizza_numeri_error():
    try:
        analizza_numeri(0, [])
        assert False
    except ValueError:
        assert True


def test_main(monkeypatch, capsys):
    inputs = iter(["5", "2", "-3", "4", "-5", "6"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    main()
    captured = capsys.readouterr()

    assert "Lista inserita: [2, -3, 4, -5, 6]" in captured.out
    assert "Positivi pari: [2, 4, 6]" in captured.out
    assert "Conteggio dispari negativi: 2" in captured.out
    assert "Media assoluta: 4.0" in captured.out
