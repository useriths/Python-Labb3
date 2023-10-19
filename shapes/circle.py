from decorators.type_enforcers import type_enforcer
from shapes.shape2d import Shape2D
from shapes.spherical import Spherical


class Circle(Spherical, Shape2D):
    @type_enforcer(valid_types=[int, float])
    def __init__(self, radius, x, y) -> None:
        Spherical.__init__(self, radius)
        Shape2D.__init__(self, x, y)

    @property
    def area(self) -> float:
        """Returns the area of the circle"""
        return self._volume()

    @property
    def circumference(self) -> float:
        """Returns the circumference of the circle"""
        return self._surface_area()

    def is_unit_circle(self) -> bool:
        """check if the circle is a unit circle. (Checking if x and y == 0 and radius == 1)"""
        return self._is_unit_shape()

    def is_inside(self, x, y) -> bool:
        """Check if (x, y) is inside the circle (on the edge does NOT count as inside)"""
        return self._is_inside(x, y)

    def __str__(self) -> str:
        return "a circle with radius={self.radius}, x={self.x} and y={self.y}"
