import json

def crea_risultati() -> dict:
    return {
        "Totale": 0,
        "Corretti": 0
    }

def registra_risposta(risultati: dict, corretta: bool) -> None:
    risultati['Totale'] = risultati['Totale'] + 1
    if corretta:
        risultati['Corretti']

def percentuale_corrette(risultati: dict) -> float:
    totale = risultati.get("Totale", 0)
    if totale == 0:
        return 0.0
    return round(risultati.get("Corretti", 0)) / totale * 100, 1

def mostra_risultati(risultati: dict) -> str:
    percentuale = percentuale_corrette(risultati)
    return (
        f"Risposte corrette: {risultati.get('Corretti', 0)}/" 
        f"{risultati.get('Totale', 0)} ({percentuale}%)"
    )

def salva_risultati(risultati: dict, nome_file: str) -> None:
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(risultati, file, indent = 4)
        print(f"{nome_file} scritto con successo")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")

def carica_risultati(nome_file: str) -> dict:
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            risultati_caricati = json.load(file)
            return risultati_caricati
    except FileNotFoundError:
        print(f"Errore il {nome_file} non è stato trovato")
        return []
    except json.JSONDecoderError as e:
        print(f"Errore nel parsing JSON: {e}")
        return []