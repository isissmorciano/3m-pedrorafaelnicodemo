# Parte 3: Implementazione di `musica/playlist.py`
# Funzioni per gestire le playlist (liste di canzoni):
# - `crea_playlist(nome: str) -> dict:` 
#   - Restituisce un dizionario con `nome` e `canzoni` (lista vuota)

from Musica import Canzoni

def crea_playlist(nome:str) -> dict:
    playlist = {
        "Nome della Playlist": nome,
        "Brani in Playlist": []
    }
    return playlist

# - `aggiungi_canzone(playlist: dict, canzone: dict) -> None:` 
#   - Aggiunge una canzone alla playlist

def aggiungi_canzone(playlist: dict, canzone: dict) -> None:
    playlist['Brani in Playlist'].append(canzone)

# - `rimuovi_canzone(playlist: dict, indice: int) -> None:` 
#   - Rimuove una canzone per indice (0-based)

def rimuovi_canzone(playlist: dict, indice: int) -> None:
    if 0 <= indice < len(playlist['Brani in Playlist']):
        playlist['Brani in Playlist'].pop(indice)
    else:
        print(f"Errore: indice {indice} non valido")

# - `durata_totale(playlist: dict) -> int:` 
#   - Restituisce durata totale in secondi
def durata_totale(playlist: dict) -> int:
    tempo_totale = 0
    for brano in playlist['Brani in Playlist']:
        tempo_totale = tempo_totale + playlist['Brani in Playlist'][brano]
        return tempo_totale

# - `mostra_playlist(playlist: dict) -> str:` 
#   - Restituisce stringa formattata con tutte le canzoni

def mostra_playlist(playlist: dict) -> str:
    if playlist['Brani in Playlist'] == []:
        return f"Nessun brano nella Playlist {playlist['Nome della Playlist']}"
    else:
        linee = [f"=== Playlist: {playlist['nome']} ==="]
    for i, canzone in enumerate(playlist['Brani in Playlist'], 1):
        linee.append(f"{i}. {info_canzone(canzone)}")

    total = durata_totale(playlist)
    minuti = total // 60
    secondi = total % 60
    linee.append(f"\nDurata totale: {minuti}:{secondi:02d}")
    
    return "\n".join(linee)