class Caretaker:
    def __init__(self):
        self._mementos = []
    
    def save(self, memento):
        self._mementos.append(memento)
    
    def load(self):
        if self._mementos:
            return self._mementos.pop()
        return None