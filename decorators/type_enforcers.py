import functools


def type_enforcer(
    valid_types,
    has_self_argument=True,
):
    """Decorator to guard against invalid argument types of a function/method."""

    def type_guard(func):
        @functools.wraps(func)
        def guard_arguments(*args, **kwargs):
            # Note that "self" is the first argument if this is called upon a method.
            args_list = args[1:] if has_self_argument else args
            has_invalid_types = not all(
                isinstance(num, tuple(valid_types)) for num in args_list
            )
            if has_invalid_types:
                type_strings = [t.__name__ for t in valid_types]
                raise TypeError(
                    f"All arguments must be of valid type ({', '.join(type_strings)})"
                )
            return func(*args, **kwargs)

        return guard_arguments

    return type_guard
