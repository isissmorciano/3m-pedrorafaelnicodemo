import json

def salva_diario(diario: dict, nome_file: str) -> None:
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(diario, file, indent = 4)
        print(f"{nome_file} scritto con successo")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")

def carica_diario(diario: dict, nome_file: str) -> None: 
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            diario = json.load(file)
            return diario
    except FileNotFoundError:
        print(f"Errore il {nome_file} non è stato trovato")
        return []
    except json.JSONDecodeError as e:
        print(f"Errore nel parsing JSON: {e}")
        return []