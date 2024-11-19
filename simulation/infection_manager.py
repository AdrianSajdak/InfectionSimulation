from math import hypot
from states.no_symptoms_state import NoSymptomsState

class InfectionManager:
    def __init__(self, infection_radius=2.0, infection_probability=0.5):
        self.infection_radius = infection_radius
        self.infection_probability = infection_probability

    def update(self, persons):
        for i, person1 in enumerate(persons):
            for person2 in persons[i+1:]:
                self._attempt_infection(person1, person2)
                self._attempt_infection(person2, person1)

    def _attempt_infection(self, infector, infectee):
        if self._can_infect(infector, infectee):
            from random import random
            if random() < self.infection_probability:
                infectee.set_state(NoSymptomsState(infectee))

    def _can_infect(self, infector, infectee):
        infectious_states = ('NoSymptomsState', 'SymptomsState')
        susceptible_states = ('HealthyState',)
        if infector.get_state().__class__.__name__ not in infectious_states:
            return False
        if infectee.get_state().__class__.__name__ not in susceptible_states:
            return False
        distance = hypot(
            infector.position.x - infectee.position.x,
            infector.position.y - infectee.position.y
        )
        return distance <= self.infection_radius
