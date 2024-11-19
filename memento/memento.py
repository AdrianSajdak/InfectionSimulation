import copy

class Memento:
    def __init__(self, state):
        self._state = copy.deepcopy(state)
    
    def get_state(self):
        return copy.deepcopy(self._state)