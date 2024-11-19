from states.istate import IState
from states.immune_state import ImmuneState

class SymptomsState(IState):
    def __init__(self, person):
        super().__init__(person)
        self.symptoms_duration = 0

    def handle(self):
        # Osobnik ma objawy choroby
        self.symptoms_duration += 1
        if self.symptoms_duration > 100:
            self.person.set_state(ImmuneState(self.person))