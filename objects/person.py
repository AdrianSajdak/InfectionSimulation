# objects/person.py

from objects.position import Position
from objects.direction import Direction
from states.istate import IState
from states.healthy_state import HealthyState
import copy

class Person:
    def __init__(self, position: Position, direction: Direction, state: IState = None):
        self.position = position
        self.direction = direction
        self.state = state if state else HealthyState(self)

    def move(self):
        # Aktualizacja pozycji
        self.position = self.position.add(self.direction)

        # Odbicie od "ścian" planszy
        if self.position.x < 0:
            self.position.x = 0
            self.direction.x *= -1
        elif self.position.x > 100:
            self.position.x = 100
            self.direction.x *= -1

        if self.position.y < 0:
            self.position.y = 0
            self.direction.y *= -1
        elif self.position.y > 100:
            self.position.y = 100
            self.direction.y *= -1

    def update_state(self):
        self.state.handle()

    def set_state(self, state: IState):
        self.state = state
        self.state.person = self

    def get_state(self):
        return self.state

    def copy(self):
        return copy.deepcopy(self)
