from decorators.type_enforcers import type_enforcer
from shapes.cubical import Cubical
from shapes.shape3d import Shape3D


class Cube(Shape3D, Cubical):
    @type_enforcer(valid_types=[int, float])
    def __init__(self, side, x, y, z) -> None:
        Shape3D.__init__(self, x=x, y=y, z=z)
        Cubical.__init__(self, side=side)

    @property
    def volume(self) -> float:
        """Returns the volume of the cube"""
        return self._volume()

    @property
    def surface_area(self) -> float:
        """Returns the surface area of the cube"""
        return (self.side**2) * 6

    @type_enforcer(valid_types=[int, float])
    def is_inside(self, x, y, z) -> bool:
        """Check if (x, y, z) is inside the cube (on the edge does NOT count as inside)"""
        return self._is_inside(x, y, z)

    def __str__(self) -> str:
        return "a cube with side={self.side}, x={self.x}, y={self.y} and z={self.z}."
