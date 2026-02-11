# Esercizio 56: Scrittura e Lettura di un File di Testo Semplice
# Obiettivo
# Creare un programma che scriva una lista di stringhe su un file e poi lo rilegga, stampando il contenuto.

# Dati forniti
# Una lista di frasi hardcoded:

# frasi = ["Ciao mondo", "Python è divertente", "File handling"]
# Istruzioni
# Definire scrivi_file(frasi, nome_file): Accetta una lista di stringhe e un nome file. Scrive ogni frase su una riga separata nel file.

# Definire leggi_file(nome_file): Accetta un nome file e restituisce una lista con le righe lette (senza newline).

# Definire main():

# Definisce frasi (dati hardcoded)
# Chiama scrivi_file per salvare su "esercizio56.txt"
# Chiama leggi_file per leggere e stampare il contenuto

# Suggerimenti
# Usa with open per aprire i file in modalità 'w' per scrittura e 'r' per lettura
# Per scrivere: file.write(frase + "\n")
# Per leggere: usa un ciclo for line in file: e .strip() per rimuovere newline
# Gestisci encoding UTF-8

# Esempio di output atteso
# Contenuto del file:
# Ciao mondo
# Python è divertente
# File handling

def scrivi_file(frasi, nome_file):
    try:
        with open(nome_file, "w", encoding= "utf-8") as file:
            for frase in frasi:
                file.write(frase + "\n")
        print(f"File {nome_file} scritto con successo")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")

def leggi_file(nome_file) -> list:
    righe = []

    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            for riga in file:
                righe.append(riga.strip())
            return righe
            
    except FileNotFoundError:
        print("Errore: il file 'esercizio56.txt' non è stato trovato")
    except IOError as e:
        print(f"Errore durante la lettura del file: {e}")

def main():
    frasi = ["Ciao mondo", "Phython è divertente", "File handling"]
    nome_file = "esercizio56.txt"
    scrivi_file(frasi, nome_file)
    righe_lette:list[str] = leggi_file(nome_file)
    for riga in righe_lette:
        print(riga)

main()