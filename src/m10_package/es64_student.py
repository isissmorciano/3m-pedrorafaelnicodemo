from Quiz import Domande, Risultati

def main() -> None:
    question_1 = Domande.crea_domanda("Testo": "Qual è il linguaggio usato in questo corso?",
                                      "Opzioni": ["Python", "Java", "C++"],
                                      "Risposta": "Phyton")
    
    question_2 = Domande.crea_domanda("Testo": "Quale materia è una materia di Scienze Integrate?",
                                      "Opzioni": ["Matematica", "Fisica", "Inglese", "Letteratura"],
                                      "Risposta": "Fisica")
    
    question_3 = Domande.crea_domanda("Testo": "Quale numero, elevato al quadrato, e poi diminuito di 5, dà come risultato 20?",
                                      "Opzioni": ["25", "12,5", "5", "√15"])
    
    domande = [question_1, question_2, question_3]
    statistiche = Risultati.crea_risultati()
    
    for domanda in domande:
        print(Domande.info_domanda(domanda))
    scelta = int(input("Seleziona (numero): "))
    if Domande.risposta_valida(domanda, scelta) is True:
        esito = Domande.verifica_risposta(domanda, scelta)
        Risultati.registra_risposta(statistiche, esito)
        print(Risultati.mostra_risultati(statistiche))
        Risultati.salva_risultati(statistiche, "Quiz_risultati,json")
    else:
        print("Errore: Risposta non valida")

if __name__=="__main__":
    main()