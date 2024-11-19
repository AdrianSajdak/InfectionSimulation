import math
from vector2d.ivector2d import IVector2D

class Vector2D(IVector2D):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def subtract(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def scale(self, scalar: float):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def magnitude(self):
        return math.hypot(self.x, self.y)
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return self.scale(1/mag)
    
    def direction(self):
        mag = self.magnitude()
        if mag == 0:
            return 0
        return math.atan2(self.y, self.x)