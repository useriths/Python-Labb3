from abc import abstractmethod

from shapes.n_dimensional_shape import NDimensionalShape


class Shape3D(NDimensionalShape):
    """Interface for all 3D shapes"""

    def __init__(self, x, y, z) -> None:
        super().__init__(x=x, y=y, z=z)

    def __lt__(self, other) -> bool:
        self._comparison_error_handler(other, Shape3D)
        return self.volume < other.volume

    def __eq__(self, other) -> bool:
        self._comparison_error_handler(other, Shape3D)
        return self.volume == other.volume

    @abstractmethod
    def is_inside(self, x, y, z) -> bool:
        ...

    @property
    @abstractmethod
    def volume(self):
        ...

    @property
    @abstractmethod
    def surface_area(self):
        ...
