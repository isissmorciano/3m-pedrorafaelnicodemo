def analizza_numeri(n: int, numeri: list[int]) -> tuple[list[int], int, float]:
    if n <= 0:
        raise ValueError("n deve essere maggiore di 0")

    positivi_pari = []
    dispari_negativi = 0
    somma_assoluti = 0

    for num in numeri:
        if num > 0 and num % 2 == 0:
            positivi_pari.append(num)
        if num < 0 and num % 2 != 0:
            dispari_negativi += 1
        somma_assoluti += abs(num)

    media_assoluta = somma_assoluti / n
    return positivi_pari, dispari_negativi, media_assoluta


def main() -> None:
    n = int(input("Quanti numeri inserire? "))
    if n <= 0:
        print("Errore: n deve essere maggiore di 0")
        return

    numeri: list[int] = []
    for i in range(n):
        numeri.append(int(input(f"Numero {i + 1}: ")))

    positivi_pari, dispari_negativi, media_assoluta = analizza_numeri(n, numeri)
    print(f"Lista inserita: {numeri}")
    print(f"Positivi pari: {positivi_pari}")
    print(f"Conteggio dispari negativi: {dispari_negativi}")
    print(f"Media assoluta: {media_assoluta}")


if __name__ == "__main__":
    main()
