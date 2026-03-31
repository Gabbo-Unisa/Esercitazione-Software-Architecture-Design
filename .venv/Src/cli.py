# src/cli.py
import operations


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
            try:
                op1 = float(input("Inserisci il primo operando: "))
                op2 = float(input("Inserisci il secondo operando: "))
            except ValueError:
                print("Errore: Devi inserire un numero reale valido. Riprova.")
                continue

            try:
                # La logica è ora delegata al modulo operations
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

            except ValueError as e:
                # Intercetta l'errore della divisione per zero sollevato da operations.py
                print(f"\nErrore Matematico: {e}")

        else:
            print("Errore: Scelta non valida. Seleziona un numero tra 0 e 4.")


if __name__ == "__main__":
    main()