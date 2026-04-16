from Diario import Entrate, Persistenza

def main() -> None:
    entrata_1 = Entrate.crea_entrata("2026-04-08", "Ho iniziato questo corso di Python", "Studio", 60)
    entrata_2 = Entrate.crea_entrata("2026-04-08", "Ho scritto un esercizio sul package diario", "Studio", 45)

    diario = Entrate.crea_diario()
    
    Entrate.aggiungi_entrata(diario, entrata_1)
    Entrate.aggiungi_entrata(diario, entrata_2)

    totale = Entrate.tempo_totale(diario)
    tempo_per_categoria = Entrate.tempo_per_categoria(diario)

    stampa = ""
    for e in diario['Entrate']:
        stampa += Entrate.info_entrata(e) + "\n"

    print(f"Diario:\n{stampa}")
    print(f"Tempo totale:\n {totale} minuti")
    print(f"Tempo per categoria:")
    for cat, tempo in tempo_per_categoria.items():
        print(f" - {cat}: {tempo} minuti")
    
    Persistenza.salva_diario(diario, "diario.json")

if __name__ == "__main__":
    main()