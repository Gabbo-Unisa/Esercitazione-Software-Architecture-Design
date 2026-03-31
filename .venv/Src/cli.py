# src/cli.py
import operations
import parser


def main():
    print("Avvio Calcolatrice...")

    while True:
        print("\n" + "=" * 30)
        print("Menu Operazioni:")
        print("1. Somma")
        print("2. Sottrazione")
        print("3. Moltiplicazione")
        print("4. Divisione")
        print("0. Esci dal programma")
        print("=" * 30)

        scelta = input("Seleziona un'operazione (0-4): ")

        if scelta == '0':
            print("Chiusura calcolatrice. Arrivederci!")
            break

        if scelta in ['1', '2', '3', '4']:
            # La CLI legge solo testo grezzo (stringhe)
            raw_op1 = input("Inserisci il primo operando: ")
            raw_op2 = input("Inserisci il secondo operando: ")

            try:
                # Deleghiamo la conversione e validazione logica al parser
                op1, op2 = parser.valida_operandi(raw_op1, raw_op2, scelta)
            except ValueError as e:
                # Intercettiamo l'errore del parser (formato errato o divisione per zero)
                print(f"Errore di Input: {e}")
                continue  # Interrompe l'iterazione corrente e torna al menu

            # Se arriviamo qui, i dati sono validi e sicuri
            if scelta == '1':
                risultato = operations.somma(op1, op2)
                print(f"\nRisultato: {op1} + {op2} = {risultato}")

            elif scelta == '2':
                risultato = operations.sottrazione(op1, op2)
                print(f"\nRisultato: {op1} - {op2} = {risultato}")

            elif scelta == '3':
                risultato = operations.moltiplicazione(op1, op2)
                print(f"\nRisultato: {op1} * {op2} = {risultato}")

            elif scelta == '4':
                risultato = operations.divisione(op1, op2)
                print(f"\nRisultato: {op1} / {op2} = {risultato}")

        else:
            print("Errore: Scelta non valida. Seleziona un numero tra 0 e 4.")


if __name__ == "__main__":
    main()