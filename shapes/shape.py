from abc import abstractmethod
from functools import total_ordering

from decorators.type_enforcers import type_enforcer
from exceptions.argument_error import ArgumentMismatchError


@total_ordering
class Shape:
    """The superclass of all shapes."""

    _dimensional_axes: list[str] = []
    _dimensions = None

    def __repr__(self) -> str:
        """Represents a Shape by the name of the class and its state.
        example: Shape(x=0, y=0)"""

        # Sort public attributes first
        attributes_sorted_by_underscore = sorted(
            self.__dict__.items(), key=lambda k: k[0].startswith("_")
        )

        attributes_string = ", ".join(
            f"{key}={value}"
            for key, value in attributes_sorted_by_underscore
            if not key.startswith("_")  # Hide protected attributes
        )
        return f"{self.__class__.__name__}({attributes_string})"

    @type_enforcer(valid_types=[int, float])
    def translate(self, *size_args) -> None:
        """Move the shape relative to its position."""
        if len(size_args) != self._dimensions:
            raise ArgumentMismatchError(
                f"Got {len(size_args)} arguments, number of arguments must be exactly {self._dimensions}"
            )

        for dimensional_arg, value in zip(self._dimensional_axes, size_args):
            setattr(self, dimensional_arg, getattr(self, dimensional_arg) + value)

    @abstractmethod
    def __lt__(self, other) -> bool:
        # Added in order to get the @total_ordering decorator to work
        ...
