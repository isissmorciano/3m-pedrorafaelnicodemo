CODICI_COMUNI = ["abc12345", "student01", "prova000", "admin999"]


def analizza_codice(codice: str) -> dict[str, int]:
    maiuscole = 0
    minuscole = 0
    cifre = 0

    for carattere in codice:
        if carattere.isupper():
            maiuscole += 1
        elif carattere.islower():
            minuscole += 1
        elif carattere.isdigit():
            cifre += 1

    return {"maiuscole": maiuscole, "minuscole": minuscole, "cifre": cifre}


def valida_codice(codice: str) -> bool:
    if len(codice) < 8:
        return False
    if not codice:
        return False
    if not codice[0].isupper():
        return False
    if codice.lower() in CODICI_COMUNI:
        return False

    conteggi = analizza_codice(codice)
    # Verifica che contenga solo lettere e cifre
    if conteggi["maiuscole"] + conteggi["minuscole"] + conteggi["cifre"] != len(codice):
        return False
    if conteggi["minuscole"] < 1:
        return False
    if conteggi["cifre"] < 1:
        return False

    return True


def livello_codice(codice: str) -> int:
    if not valida_codice(codice):
        return 0

    livello = 1
    if len(codice) >= 10:
        livello += 1

    conteggi = analizza_codice(codice)
    if conteggi["maiuscole"] > 1 or conteggi["cifre"] > 1:
        livello += 1

    return livello


def main() -> None:
    codice = input("Inserisci un codice alfanumerico: ").strip()
    if valida_codice(codice):
        print(f"Valido (Livello {livello_codice(codice)})")
    else:
        print("Non valido")


if __name__ == "__main__":
    main()
