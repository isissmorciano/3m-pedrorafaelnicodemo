# Esercizio 57: Conteggio Parole in un File
# Obiettivo
# Leggere un file di testo e contare le occorrenze di ogni parola (case-insensitive, ignorando punteggiatura semplice).

# Dati forniti
# Un paragrafo hardcoded da scrivere su file:

# testo = "Python è un linguaggio di programmazione. Python è semplice e potente."
# Istruzioni
# Definire conta_parole(nome_file): Accetta un nome file, legge il contenuto, splitta in parole (ignorando maiuscole e punteggiatura come virgole e punti), e restituisce un dizionario {parola: conteggio}.

# Definire stampa_conteggio(dizionario): Accetta il dizionario e lo stampa in ordine alfabetico delle chiavi.

# Definire main():
# Definisce testo (dati hardcoded)
# Scrive testo su "esercizio57.txt"
# Chiama conta_parole e stampa_conteggio

# Suggerimenti
# Per scrivere il file iniziale: usa with open("esercizio57.txt", "w") as f: f.write(testo)
# Per contare: converti tutto in lowercase, rimuovi "." e ",", poi .split()
# Usa un dizionario per accumulare conteggi
# Per ordinare: sorted(dizionario.items())

# Esempio di output atteso
# Conteggio parole:
# di: 1
# e: 1
# linguaggio: 1
# potente: 1
# programmazione: 1
# python: 2
# semplice: 1
# un: 1
# è: 2

def conta_parole(nome_file: str) -> dict[str, int]:
    conteggio = {}
    try:
        with open(nome_file, "r", encoding= "utf-8") as file:
            file.read().lower()
            contenuto = contenuto.replace(".","").replace(",", "")
            parole = contenuto.split()
            for parola in parole:
                if parola in conteggio:
                    conteggio[parola] = + 1
                else: 
                    conteggio[parola] = 1

    except FileNotFoundError:
        print("Errore: il file 'esercizio57.txt' non è stato trovato")
    except IOError as e:
        print(f"Errore durante la lettura del file:{e}")

def stampa_conteggio(dizionario):
    for parola, numero in sorted(dizionario.items()):
        print(f"{parola}: {numero}")

def main():
    testo = "Phython è un linguaggio di programmazione. Phython è semplice e potente."
    nome_file = "esercizio57.txt"

    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            file.write(testo)
        print(f"File '{nome_file}' creato con successo.")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")
        return
    
    dizionario_conteggio = conta_parole(nome_file)
    stampa_conteggio(dizionario_conteggio)
    conta_parole(nome_file)

if __name__ == "__main__":
    main()