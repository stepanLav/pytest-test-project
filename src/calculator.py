import os

class Calculator:
    def __init__(self, max_history_size=None):
        self.history = []
        self.max_history_size = max_history_size or os.getenv('CALCULATOR_MAX_HISTORY', None)
        if self.max_history_size is not None:
            self.max_history_size = int(self.max_history_size)
            
    def _add_to_history(self, entry):
        self.history.append(entry)
        if self.max_history_size and len(self.history) > self.max_history_size:
            self.history.pop(0)

    def add(self, a, b):
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self._add_to_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._add_to_history(f"{a} / {b} = {result}")
        return result

    def clear_history(self):
        self.history = []
