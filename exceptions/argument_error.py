class ArgumentMismatchError(Exception):
    """Exception class for mismatching arguments."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
