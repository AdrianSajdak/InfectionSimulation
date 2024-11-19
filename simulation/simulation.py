# simulation/simulation.py

from objects.person import Person
from objects.position import Position
from objects.direction import Direction
from states.healthy_state import HealthyState
from states.immune_state import ImmuneState
from states.no_symptoms_state import NoSymptomsState
from memento.memento import Memento
from memento.caretaker import Caretaker
from simulation.infection_manager import InfectionManager
from visualization.visualizer import Visualizer
import random
import time

class Simulation:
    def __init__(self):
        self.persons = []
        self.infection_manager = InfectionManager()
        self.caretaker = Caretaker()
        self.visualizer = Visualizer()
        self.time_step = 0.04  # 25 kroków na sekundę

    def initialize(self, immunity_rate=0.0):
        num_persons = 30  # Zmniejszono liczbę osobników
        for _ in range(num_persons):
            x = random.uniform(0, 100)
            y = random.uniform(0, 100)
            direction = Direction()
            if random.random() < immunity_rate:
                state = ImmuneState(None)
            else:
                state = HealthyState(None)
            position = Position(x, y)
            person = Person(position, direction, state)
            state.person = person
            self.persons.append(person)

        initial_infected = random.sample(self.persons, k=3)
        for person in initial_infected:
            infected_state = NoSymptomsState(person)
            person.set_state(infected_state)

    def run(self):
        steps_per_second = 25
        delay = 1.0 / steps_per_second
        while True:
            start_time = time.time()
            self.update()
            self.render()
            elapsed_time = time.time() - start_time
            sleep_time = max(0, delay - elapsed_time)
            time.sleep(sleep_time)

    def update(self):
        for person in self.persons:
            person.move()
            person.update_state()
        self.infection_manager.update(self.persons)

    def render(self):
        self.visualizer.render(self.persons)

    def save_state(self):
        memento = Memento(self.persons)
        self.caretaker.save(memento)

    def load_state(self):
        memento = self.caretaker.load()
        if memento:
            self.persons = memento.get_state()
