from math import prod

from decorators.type_enforcers import type_enforcer
from exceptions.argument_error import ArgumentMismatchError


class Cuboidal:
    """Cuboidal is a superclass for all rectangle/cuboid like shapes.
    All cuboidal shapes are have N dimensions and N sides.
    This class shouldn't be instantiated."""

    def __init__(self, **sides) -> None:
        self.__dict__ |= sides
        self._side_names = list(sides.keys())

    def _volume(self) -> float:
        """Returns the volume of an cuboidal shape."""
        return prod(getattr(self, side) for side in self._side_names)

    @type_enforcer(valid_types=[int, float])
    def resize(self, *new_sides) -> None:
        """Resizes the cuboidal."""
        if len(new_sides) != self._dimensions:
            raise ArgumentMismatchError(
                f"Got {len(new_sides)} arguments, number of arguments must be exactly {self._dimensions}"
            )

        for side_name, side_value in zip(self._side_names, new_sides):
            setattr(self, side_name, side_value)

    def _is_regular(self) -> bool:
        """Check if this cuboidal is regular (Cubical), with all sides equal."""
        side_equality_list = []
        for side_name in self._side_names:
            side_value = getattr(self, side_name)
            first_value = getattr(self, self._side_names[0])
            side_equality_list.append(side_value == first_value)

        return all(side_equality_list)

    @type_enforcer(valid_types=[int, float])
    def _is_inside(self, *dimensional_args) -> bool:
        """Checks if a point in N dimensions is inside the cuboidal shape."""
        if len(dimensional_args) != self._dimensions:
            raise ArgumentMismatchError(
                f"Got {len(dimensional_args)} arguments, number of arguments must be exactly {self._dimensions}"
            )

        instance_coordinates = [getattr(self, axis) for axis in self._dimensional_axes]

        instance_sides = [getattr(self, side) for side in self._side_names]

        coordinates = zip(instance_coordinates, instance_sides, dimensional_args)

        return all(
            (coodinate - (side / 2)) < argument < (coodinate + (side / 2))
            for coodinate, side, argument in coordinates
        )
