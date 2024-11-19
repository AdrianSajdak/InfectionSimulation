from abc import ABC, abstractmethod

class IState(ABC):
    def __init__(self, person):
        self.person = person

    @abstractmethod
    def handle(self):
        pass