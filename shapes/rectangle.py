from decorators.type_enforcers import type_enforcer
from shapes.cuboidal import Cuboidal
from shapes.shape2d import Shape2D


class Rectangle(Shape2D, Cuboidal):
    @type_enforcer(valid_types=[int, float])
    def __init__(self, x, y, side1, side2) -> None:
        Shape2D.__init__(self, x=x, y=y)
        Cuboidal.__init__(self, side1=side1, side2=side2)

    @property
    def area(self) -> float:
        """Returns the area of the rectangle"""
        return self._volume()

    @property
    def perimeter(self) -> float:
        """Returns the perimeter of the rectangle"""
        return (self.side1 * 2) + (self.side2 * 2)

    def is_square(self) -> bool:
        """Check if the rectangle is a square."""
        return self._is_regular()

    @type_enforcer(valid_types=[int, float])
    def is_inside(self, x, y) -> bool:
        """Check if (x, y) is inside the rectangle (on the edge does NOT count as inside)"""
        return self._is_inside(x, y)

    def __str__(self) -> str:
        return "a rectangle with side1={self.side1}, side2={self.side2}, x={self.x} and y={self.y}"
