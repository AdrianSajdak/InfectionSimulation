from states.istate import IState
from states.immune_state import ImmuneState

class InfectedState(IState):
    def __init__(self, person):
        self.person = person
        self.infection_duration = 0
    
    def handle(self):
        # Logika dla stanu zakażonego
        self.infection_duration += 1
        if self.infection_duration > 100:
            self.person.set_state(ImmuneState(self.person))