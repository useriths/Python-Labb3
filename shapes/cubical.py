from decorators.type_enforcers import type_enforcer
from exceptions.argument_error import ArgumentMismatchError


class Cubical:
    """Cubical is a superclass for all square/cube like shapes.
    All cubical shapes are regular N-dimensional cubicals.
    This class shouldn't be instantiated."""

    def __init__(self, side) -> None:
        self.side = side

    def _surface_area(self) -> float:
        ...

    def _volume(self) -> float:
        """Returns the volume of an N dimensional cubical shape."""
        return self.side**self._dimensions

    @type_enforcer(valid_types=[int, float])
    def resize(self, side) -> None:
        """Changes the value of the side"""
        self.side = side

    @type_enforcer(valid_types=[int, float])
    def _is_inside(self, *dimensional_args) -> bool:
        """Checks if a point in N dimensions is inside the cubical shape."""
        if len(dimensional_args) != self._dimensions:
            raise ArgumentMismatchError(
                f"Got {len(dimensional_args)} arguments, number of arguments must be exactly {self._dimensions}"
            )
        half_side = self.side / 2

        instance_coordinates = [getattr(self, axis) for axis in self._dimensional_axes]

        coordinates = zip(instance_coordinates, dimensional_args)

        return all(
            (coordinate - half_side) < argument < (coordinate + half_side)
            for coordinate, argument in coordinates
        )
