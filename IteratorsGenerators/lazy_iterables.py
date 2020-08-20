from dataclasses import dataclass
from math import pi

@dataclass
class Circle:
    _radius:float
    _area:float = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = pi * (self.radius**2)
        return self._area


if __name__ == "__main__":
    circle = Circle(1)
    print(circle.radius)
    print(circle.area)

    circle.radius = 3
    print(circle.radius)
    print(circle.area)
