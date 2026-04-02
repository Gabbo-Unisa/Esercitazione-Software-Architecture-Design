# src/cli.py

import operations
import parser
from calculator import Calculator

def leggi_operando(messaggio: str, calc: Calculator) -> float:
    """
    Legge l'input dell'utente. Se l'utente digita 'MR', recupera il
    valore dalla memoria, altrimenti converte l'input in numero.
    """
    raw_val = input(messaggio).strip().upper()
    
    if raw_val == 'MR':
        if calc.has_memory():
            mem_val = calc.memory_recall()
            print(f" -> Valore richiamato dalla memoria: {mem_val}")
            return mem_val
        else:
            raise ValueError("Il registro di memoria è vuoto.")
            
    # Se non è MR, procede con la normale conversione usando il parser
    return parser.converti_in_float(raw_val)

def main():
    calc = Calculator()
    print("Avvio Calcolatrice Scientifica...")
    
    while True:
        print("\n" + "="*35)
        # Mostra lo stato dell'accumulatore (Risultato corrente)
        if calc.has_result():
            print(f"RISULTATO CORRENTE: {calc.current_value}")
        else:
            print("Nessun valore in memoria principale")
            
        # Mostra lo stato del registro di Memoria
        stato_memoria = calc.memory_recall() if calc.has_memory() else "Vuota"
        print(f"REGISTRO MEMORIA  : {stato_memoria}")
            
        print("-" * 35)
        print("1. Somma        2. Sottrazione")
        print("3. Moltiplicaz. 4. Divisione")
        print("5. SIN          6. COS")
        print("7. TAN          8. LOG")
        print("M+. Salva Mem   MC. Cancella Mem")
        print("R. Reset Totale 0. Esci")
        print("(Usa 'MR' al posto di un numero per usare la memoria)")
        print("="*35)
        
        scelta = input("Seleziona un'opzione: ").strip().upper()
        
        if scelta == '0':
            print("Chiusura. Arrivederci!")
            break
            
        if scelta == 'R':
            calc.reset()
            print("Accumulatore azzerato.")
            continue
            
        # --- LOGICA MEMORIA (M+ e MC) ---
        if scelta == 'M+':
            try:
                calc.memory_save()
                print(f"Valore {calc.memory_recall()} salvato in memoria.")
            except ValueError as e:
                print(f"\nERRORE: {e}")
            continue
            
        if scelta == 'MC':
            calc.memory_clear()
            print("Registro di memoria cancellato.")
            continue

        # --- LOGICA OPERAZIONI MATEMATICHE ---
        if scelta in ['1', '2', '3', '4', '5', '6', '7', '8']:
            try:
                # 1° Operando
                if calc.has_result():
                    op1 = calc.current_value
                    print(f"Valore in uso: {op1}")
                else:
                    op1 = leggi_operando("Inserisci il numero (o 'MR'): ", calc)
                
                # Operazioni Aritmetiche Base (richiedono 2° operando)
                if scelta in ['1', '2', '3', '4']:
                    op2 = leggi_operando("Inserisci il secondo numero (o 'MR'): ", calc)
                    
                    if scelta == '4':
                        parser.valida_divisione(op2)
                    
                    if scelta == '1': risultato = operations.somma(op1, op2)
                    elif scelta == '2': risultato = operations.sottrazione(op1, op2)
                    elif scelta == '3': risultato = operations.moltiplicazione(op1, op2)
                    elif scelta == '4': risultato = operations.divisione(op1, op2)
                
                # Operazioni Scientifiche
                else:
                    if scelta == '5': risultato = operations.sin(op1)
                    elif scelta == '6': risultato = operations.cos(op1)
                    elif scelta == '7': risultato = operations.tan(op1)
                    elif scelta == '8': risultato = operations.log(op1)
                    
                    risultato = round(risultato, 4)
                
                # Aggiornamento stato
                calc.set_result(risultato)
                print(f"\n>>> RISULTATO: {risultato}")
                
            except ValueError as e:
                print(f"\nERRORE: {e}")
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()