# Implementazione delle singole operazioni
# src/operations.py

import math

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

def sin(value):
    # Assumiamo che l'utente inserisca i gradi
    return math.sin(math.radians(value))

def cos(value):
    return math.cos(math.radians(value))

def tan(value):
    # Controllo per la restrizione: tangente di 90° (e multipli dispari)
    if value % 180 == 90:
        raise ValueError("Errore matematico: tangente non definita per questo angolo.")
    return math.tan(math.radians(value))

def log(value):
    # Controllo per la restrizione: logaritmo di un numero negativo o zero
    if value <= 0:
        raise ValueError("Errore matematico: logaritmo definito solo per numeri positivi.")
    return math.log10(value) # Assumiamo logaritmo in base 10