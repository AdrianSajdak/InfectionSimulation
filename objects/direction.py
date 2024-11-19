# objects/direction.py

import random
import math
from vector2d.vector2d import Vector2D

class Direction(Vector2D):
    def __init__(self, x: float = None, y: float = None):
        if x is None or y is None:
            angle = random.uniform(0, 2 * math.pi)
            x = math.cos(angle)
            y = math.sin(angle)
        super().__init__(x, y)
        self.normalize()
        self.scale(0.5)  # Dostosowanie prędkości ruchu

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            self.x, self.y = 0, 0
        else:
            self.x /= mag
            self.y /= mag

    def scale(self, scalar: float):
        self.x *= scalar
        self.y *= scalar
