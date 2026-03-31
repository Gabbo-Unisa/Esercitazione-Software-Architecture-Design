# Implementazione delle singole operazioni
# src/operations.py

def somma(a: float, b: float) -> float:
    return a + b

def sottrazione(a: float, b: float) -> float:
    return a - b

def moltiplicazione(a: float, b: float) -> float:
    return a * b

def divisione(a: float, b: float) -> float:
    if b == 0:
        # Solleviamo un'eccezione invece di fare una print,
        # sarà il CLI a decidere come mostrare l'errore all'utente.
        raise ValueError("La divisione per zero non è ammissibile.")
    return a / b