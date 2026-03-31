# src/calculator.py

class Calculator:
    def __init__(self):
        # Inizializziamo a None per indicare che non c'è ancora un calcolo in memoria
        self._current_value = None

    @property
    def current_value(self):
        """Restituisce il valore attualmente in memoria."""
        return self._current_value

    def set_result(self, value: float):
        """Salva il nuovo risultato in memoria."""
        self._current_value = value

    def reset(self):
        """Azzera la memoria della calcolatrice."""
        self._current_value = None

    def has_result(self) -> bool:
        """Verifica se c'è un risultato salvato in memoria."""
        return self._current_value is not None