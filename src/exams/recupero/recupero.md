# Verifica di Recupero - 2 Esercizi

## Consegna
Consegna un file Python rinominato come `cognome.py` (es. `rossi.py`).

---

## Esercizio 1
Chiedi quanti numeri inserire (`n > 0`), leggi i numeri e salvali in una lista.

Il programma deve:
- creare una lista con i numeri positivi e pari;
- contare i numeri dispari negativi;
- calcolare la media assoluta dei numeri;
- stampare lista inserita, lista filtrata, conteggio e media.

### Esempio
Input: `2, -3, 4, -5, 6`

Output:
- `Lista inserita: [2, -3, 4, -5, 6]`
- `Positivi pari: [2, 4, 6]`
- `Conteggio dispari negativi: 2`
- `Media assoluta: 4.0`

---

## Esercizio 2
Verifica un codice alfanumerico (solo lettere e cifre) con queste regole:
- almeno 8 caratteri;
- primo carattere maiuscolo;
- almeno una lettera minuscola;
- almeno una cifra;
- contiene solo lettere e cifre (niente spazi o caratteri speciali);
- non deve essere nella lista `CODICI_COMUNI = ["abc12345", "student01", "prova000", "admin999"]`.

### Istruzioni
Definisci le funzioni:
- `analizza_codice(codice: str) -> dict[str, int]`: conta quante lettere maiuscole, minuscole e cifre ci sono nel codice e restituisce un dizionario con queste chiavi:
	- `"maiuscole"`
	- `"minuscole"`
	- `"cifre"`
  
	Esempio: per `Abc12346` deve restituire qualcosa come `{"maiuscole": 1, "minuscole": 2, "cifre": 5}`.
- `valida_codice(codice: str) -> bool`: controlla se il codice rispetta tutte le regole e restituisce `True` oppure `False`. Per verificare che contenga solo lettere e cifre, puoi controllare che la somma (maiuscole + minuscole + cifre) sia uguale alla lunghezza del codice.
- `livello_codice(codice: str) -> int`: assegna un livello da 1 a 3 in base alla lunghezza e al numero di maiuscole o cifre.

Nel `main()`, chiedi il codice e stampa:
- `Valido (Livello X)` se è valido;
- `Non valido` altrimenti.

### Esempio
Input: `Abc12346`

Output: `Valido (Livello 2)`