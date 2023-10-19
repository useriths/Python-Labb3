class DimensionalMismatchError(Exception):
    """Exception class for dimensional errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
