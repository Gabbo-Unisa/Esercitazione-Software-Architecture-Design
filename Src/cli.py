import operations
import parser
from calculator import Calculator

def main():
    calc = Calculator()
    print("Avvio Calcolatrice Scientifica...")
    
    while True:
        print("\n" + "="*30)
        # Mostra lo stato corrente
        if calc.has_result():
            print(f"RISULTATO CORRENTE: {calc.current_value}")
        else:
            print("Nessun valore in memoria (Inizia un nuovo calcolo)")
            
        print("-" * 30)
        print("1. Somma        2. Sottrazione")
        print("3. Moltiplicaz. 4. Divisione")
        print("5. SIN          6. COS")
        print("7. TAN          8. LOG")
        print("R. Reset        0. Esci")
        print("="*30)
        
        scelta = input("Seleziona un'opzione: ").upper()
        
        if scelta == '0':
            print("Chiusura. Arrivederci!")
            break
            
        if scelta == 'R':
            calc.reset()
            print("Memoria azzerata.")
            continue

        if scelta in ['1', '2', '3', '4', '5', '6', '7', '8']:
            try:
                # Logica per il primo operando (o l'unico operando per le scientifiche)
                if calc.has_result():
                    op1 = calc.current_value
                    print(f"Valore in uso: {op1}")
                else:
                    raw_op1 = input("Inserisci il numero: ")
                    op1 = parser.converti_in_float(raw_op1)
                
                # SEPARAZIONE LOGICA: Operazioni Aritmetiche Base
                if scelta in ['1', '2', '3', '4']:
                    raw_op2 = input("Inserisci il secondo numero: ")
                    op2 = parser.converti_in_float(raw_op2)
                    
                    if scelta == '4':
                        parser.valida_divisione(op2)
                    
                    if scelta == '1': risultato = operations.somma(op1, op2)
                    elif scelta == '2': risultato = operations.sottrazione(op1, op2)
                    elif scelta == '3': risultato = operations.moltiplicazione(op1, op2)
                    elif scelta == '4': risultato = operations.divisione(op1, op2)
                
                # SEPARAZIONE LOGICA: Operazioni Scientifiche
                else:
                    if scelta == '5': risultato = operations.sin(op1)
                    elif scelta == '6': risultato = operations.cos(op1)
                    elif scelta == '7': risultato = operations.tan(op1)
                    elif scelta == '8': risultato = operations.log(op1)
                    
                    # Applica la precisione di almeno 4 decimali per le scientifiche
                    risultato = round(risultato, 4)
                
                # Aggiornamento stato: avviene SOLO se non ci sono state eccezioni.
                # Questo soddisfa il criterio di mantenere l'accumulatore invariato in caso di errore.
                calc.set_result(risultato)
                print(f"\n>>> RISULTATO: {risultato}")
                
            except ValueError as e:
                # In caso di errore matematico (es. LOG di numero negativo o Divisione per zero)
                # l'eccezione viene catturata qui, stampata, e il set_result() viene ignorato.
                print(f"\nERRORE: {e}")
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()