from abc import abstractmethod

from exceptions.dimensional_error import DimensionalMismatchError
from shapes.shape import Shape


class NDimensionalShape(Shape):
    """Constructs the structure for an N-Dimensional Shape"""

    def __init__(self, **dimensional_args) -> None:
        self.__dict__ |= dimensional_args
        self._dimensional_axes = list(dimensional_args.keys())
        self._dimensions = len(self._dimensional_axes)

    def _comparison_error_handler(self, other, class_type) -> None:
        """Error handler to check if the dimensions are compatible"""
        if (not issubclass(self.__class__, class_type)) or (
            not issubclass(other.__class__, class_type)
        ):
            raise DimensionalMismatchError(
                f"Can only compare a {class_type.__name__} with another {class_type.__name__}."
            )

    @abstractmethod
    def is_inside(self, *dimensional_args) -> bool:
        ...

    @property
    def volume(self):
        ...

    @property
    def surface_area(self):
        ...
