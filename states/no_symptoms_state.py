from states.istate import IState
from states.symptoms_state import SymptomsState

class NoSymptomsState(IState):
    def __init__(self, person):
        super().__init__(person)
        self.incubation_period = 0

    def handle(self):
        # Osobnik jest zakażony bezobjawowo
        self.incubation_period += 1
        if self.incubation_period > 50:
            self.person.set_state(SymptomsState(self.person))