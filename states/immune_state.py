from states.istate import IState
from states.healthy_state import HealthyState

class ImmuneState(IState):
    def __init__(self, person):
        super().__init__(person)
        self.immunity_duration = 0

    def handle(self):
        # Osobnik jest odporny po chorobie
        self.immunity_duration += 1
        if self.immunity_duration > 200:
            self.person.set_state(HealthyState(self.person))