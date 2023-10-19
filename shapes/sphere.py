from decorators.type_enforcers import type_enforcer
from shapes.shape3d import Shape3D
from shapes.spherical import Spherical


class Sphere(Spherical, Shape3D):
    @type_enforcer(valid_types=[int, float])
    def __init__(self, radius, x, y, z) -> None:
        Spherical.__init__(self, radius)
        Shape3D.__init__(self, x, y, z)

    @property
    def volume(self) -> float:
        """Returns the volume of the sphere"""
        return self._volume()

    @property
    def surface_area(self) -> float:
        """Returns the surface area of the sphere"""
        return self._surface_area()

    def is_unit_sphere(self) -> bool:
        """check if the circle is a unit sphere. (Checking if x, y and z == 0 and radius == 1)"""
        return self._is_unit_shape()

    def is_inside(self, x, y, z) -> bool:
        """Check if (x, y, z) is inside the cube (on the edge does NOT count as inside)"""
        return self._is_inside(x, y, z)

    def __str__(self) -> str:
        return "a sphere with radius={self.radius}, x={self.x}, y={self.y} and z={self.z}"
