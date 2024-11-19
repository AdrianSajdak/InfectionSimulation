from abc import ABC, abstractmethod

class IVector2D(ABC):
    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def subtract(self, other):
        pass

    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def magnitude(self):
        pass

    @abstractmethod
    def normalize(self):
        pass

    @abstractmethod
    def direction(self):
        pass