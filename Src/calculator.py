# src/calculator.py

class Calculator:
    def __init__(self):
        # Inizializziamo a None per indicare che non c'è ancora un calcolo in memoria
        self._current_value = None
        # Inizializziamo il registro di memoria a vuoto
        self._memory = None
        self.history = []  # Memorizza le stringhe delle operazioni

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

    def aggiungi_operazione(self, op1, operatore, op2=None, risultato=None):
        """
        Crea la stringa dell'operazione e la aggiunge alla cronologia.
        Gestisce sia operazioni a due operandi che a un operando.
        """
        if op2 is not None:
            # Esempio: "5.0 + 3.0 = 8.0"
            stringa_op = f"{op1} {operatore} {op2} = {risultato}"
        else:
            # Esempio: "SIN(90.0) = 1.0"
            stringa_op = f"{operatore}({op1}) = {risultato}"

        self.history.append(stringa_op)

    def get_contesto_recente(self):
        """
        Ritorna le ultime 3 operazioni (US6).
        Se sono meno di 3, ritorna quelle disponibili.
        """
        return self.history[-3:]