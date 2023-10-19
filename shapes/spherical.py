"""Volume and Surface Area of an N-dimensional sphere with specified radius.
Can be used for both circles and spheres.
Read more at: https://en.wikipedia.org/wiki/N-sphere#Volume_and_surface_area"""

import math

from decorators.type_enforcers import type_enforcer
from exceptions.argument_error import ArgumentMismatchError


class InstatiationError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Spherical:
    def __init__(self, radius):
        if self.__class__ == Spherical:
            raise InstatiationError(
                f"Only subclasses of '{self.__class__.__name__}' should be instantiated."
            )
        self.radius = radius
        self._pi = 3.1415926535897932384626

    def _is_unit_shape(self) -> bool:
        """Return True if all dimensional coordinates are at origo and the radius is 1."""
        if self.radius != 1:
            return False

        dimensional_values = [getattr(self, attr) for attr in self._dimensional_axes]

        return all(coodinate == 0 for coodinate in dimensional_values)

    def _surface_area(self) -> float:
        """Return the surface area of an N-dimensional sphere with given radius."""
        return (
            (2 * (self._pi ** (self._dimensions / 2)))
            / math.gamma(self._dimensions / 2)
        ) * (self.radius ** (self._dimensions - 1))

    def _volume(self) -> float:
        """Return the volume of an N-dimensional sphere with given radius."""
        return (
            (self._pi ** (self._dimensions / 2))
            / math.gamma((self._dimensions / 2) + 1)
        ) * (self.radius**self._dimensions)

    @type_enforcer(valid_types=[int, float])
    def resize(self, radius) -> None:
        self.radius = radius

    @type_enforcer(valid_types=[int, float])
    def _is_inside(self, *dimensional_args) -> bool:
        if len(dimensional_args) != self._dimensions:
            raise ArgumentMismatchError(
                f"Got {len(dimensional_args)} arguments, number of arguments must be exactly {self._dimensions}"
            )

        # The objects own coordinate offsets
        instance_coordinates = [getattr(self, axis) for axis in self._dimensional_axes]

        coordinates = zip(instance_coordinates, dimensional_args)

        total_distance = math.sqrt(
            sum((offset - coordinate) ** 2 for offset, coordinate in coordinates)
        )

        return total_distance < self.radius
