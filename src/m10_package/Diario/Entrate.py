
def crea_entrata(data: str, testo: str, categoria: str, durata: int) -> dict:
    return {
        "Data": data,
        "Testo": testo,
        "Categoria": categoria,
        "Durata": durata
    }

def info_entrata(entrata: dict) -> str:
    return f"\n{entrata['Data']} [{entrata['Categoria']}] ({entrata['Durata']} min): {entrata['Testo']}"

def crea_diario() -> dict:
    return {"Entrate": []}

def aggiungi_entrata(diario: dict, entrata: dict) -> None:
    diario['Entrate'].append(entrata)

def rimuovi_entrata(diario: dict, indice: int):
    if 0 <= indice < len(diario['Entrate']):
        diario['Entrate'].pop(indice)
    else:
        print(f"Errore: Indice {indice} non valido!")

def tempo_totale(diario: dict) -> int:
    return sum(entrata['Durata'] for entrata in diario['Entrate'])

def tempo_per_categoria(diario: dict) -> dict[str, int]:
    filtrare = {}
    for entrata in diario['Entrate']:
        categoria = entrata['Categoria']
        durata = entrata['Durata']
        if categoria in filtrare:
            filtrare['Categoria'] = filtrare['Categoria'] + durata
        else:
            filtrare['Categoria'] = durata
    return filtrare

def trova_entrate_per_data(diario: dict, data: str) -> list[dict]:
    filtrare = []
    for entrata in diario['Entrate']:
        if entrata['Data'] == data:
            filtrare.append(entrata)
    return filtrare