# Interpreta l'input testuale dell'utente
# src/parser.py

def converti_in_float(raw_val: str) -> float:
    """
    Converte una stringa in un numero in virgola mobile.
    """
    try:
        return float(raw_val)
    except ValueError:
        raise ValueError(f"'{raw_val}' non è un numero valido.")


def valida_divisione(divisore: float):
    """
    Verifica che il divisore non sia zero.
    """
    if divisore == 0.0:
        raise ValueError("Errore Matematico: Il divisore non può essere zero.")


def valida_logaritmo(valore: float):
    """
    Verifica che l'argomento del logaritmo sia strettamente positivo.
    """
    if valore <= 0:
        raise ValueError("Errore Matematico: Il logaritmo è definito solo per numeri positivi (> 0).")


def valida_tangente(gradi: float):
    """
    Verifica che l'angolo sia valido per la tangente (esclude 90°, 270°, ecc.).
    """
    if gradi % 180 == 90:
        raise ValueError("Errore Matematico: La tangente non è definita per 90° e i suoi multipli dispari.")


def valida_operandi(raw_op1: str, raw_op2: str = "0", scelta_operazione: str = "") -> tuple[float, float]:
    """
    Converte le stringhe in ingresso in numeri reali (float) e
    valida la logica dei parametri in base all'operazione.
    """
    op1 = converti_in_float(raw_op1)
    
    # Le opzioni da 5 a 8 (scientifiche) richiedono un solo operando.
    # Restituiamo op1 e ignoriamo op2.
    if scelta_operazione in ['5', '6', '7', '8']:
        if scelta_operazione == '7':
            valida_tangente(op1)
        elif scelta_operazione == '8':
            valida_logaritmo(op1)
        return op1, 0.0

    # Per le operazioni aritmetiche base (1, 2, 3, 4) serve anche il secondo operando
    op2 = converti_in_float(raw_op2)

    if scelta_operazione == '4':
        valida_divisione(op2)

    return op1, op2