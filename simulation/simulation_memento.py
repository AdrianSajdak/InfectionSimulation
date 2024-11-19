import copy

class SimulationMemento:
    def __init__(self, persons_state):
        self._state = copy.deepcopy(persons_state)
    
    def get_state(self):
        return copy.deepcopy(self._state)