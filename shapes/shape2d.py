from abc import abstractmethod

from shapes.n_dimensional_shape import NDimensionalShape


class Shape2D(NDimensionalShape):
    """Interface for all 2D shapes"""

    def __init__(self, x, y) -> None:
        super().__init__(x=x, y=y)

    def __lt__(self, other) -> bool:
        self._comparison_error_handler(other, Shape2D)
        return self.area < other.area

    def __eq__(self, other) -> bool:
        self._comparison_error_handler(other, Shape2D)
        return self.area == other.area

    @abstractmethod
    def is_inside(self, x, y) -> bool:
        ...

    @property
    @abstractmethod
    def area(self):
        ...
