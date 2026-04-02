# src/calculator.py

class Calculator:
    def __init__(self):
        # Inizializziamo a None per indicare che non c'è ancora un calcolo in memoria
        self._current_value = None
        # Inizializziamo il registro di memoria a vuoto
        self._memory = None 

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
    
    # --- NUOVE FUNZIONI DI MEMORIA [US5] ---

    def memory_save(self):
        """Salva il valore corrente nel registro di memoria (M+)"""
        if self.has_result():
            self._memory = self._current_value
        else:
            raise ValueError("Nessun valore nell'accumulatore da salvare in memoria.")

    def memory_recall(self):
        """Restituisce il valore salvato nel registro di memoria (MR)"""
        return self._memory

    def memory_clear(self):
        """Azzera solo il registro di memoria (MC)"""
        self._memory = None

    def has_memory(self) -> bool:
        """Verifica se c'è un valore salvato in memoria"""
        return self._memory is not None