# Parte 2: Implementazione di `musica/canzoni.py`
# Funzioni per gestire le canzoni (rappresentate come dizionari):
# - `crea_canzone(titolo: str, artista: str, durata: int) -> dict:` 
#   - Restituisce un dizionario con chiavi: `titolo`, `artista`, `durata`

def crea_canzone(titolo: str, artista: str, durata:int) -> dict:
    return {
        "Titolo del brano": titolo,
        "Artista": artista,
        "Durata": durata 
    }

# - `info_canzone(canzone: dict) -> str:` 
#   - Restituisce formato: `"Titolo - Artista (M:SS)"`
#   - Esempio: `"Bohemian Rhapsody - Queen (5:55)"`

def info_canzone(canzone: dict) -> str:
    titolo = canzone['Titolo del brano']
    artista = canzone['Artista']
    durata = canzone['durata']
    print(f"{titolo} - {artista} ({durata})")