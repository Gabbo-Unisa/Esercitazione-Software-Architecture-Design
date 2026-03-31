# Interpreta l'input testuale dell'utente
# src/parser.py

def valida_operandi(raw_op1: str, raw_op2: str, scelta_operazione: str) -> tuple[float, float]:
    """
    Converte le stringhe in ingresso in numeri reali (float) e
    valida la logica dei parametri in base all'operazione.
    """
    try:
        op1 = float(raw_op1)
        op2 = float(raw_op2)
    except ValueError:
        # Se la conversione fallisce (es. l'utente ha inserito lettere)
        raise ValueError("I valori inseriti non sono numeri reali validi.")

    # Controllo specifico per la divisione (scelta '4')
    if scelta_operazione == '4' and op2 == 0.0:
        raise ValueError("Impossibile eseguire la divisione: il divisore non può essere zero.")

    return op1, op2