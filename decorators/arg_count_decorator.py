import functools

from exceptions.argument_error import ArgumentMismatchError


def arg_count_enforcer(
    number_of_arguments,
    has_self_argument=True,
):
    """Decorator to guard against invalid number of argument of a function/method."""

    def count_guard(func):
        @functools.wraps(func)
        def guard_arguments(*args, **kwargs):
            # Note that "self" is the first argument if this is called upon a method.
            args_list = args[1:] if has_self_argument else args
            if len(args_list) != number_of_arguments:
                raise ArgumentMismatchError(
                    f"Got {len(args_list)} arguments, number of arguments must be exactly {number_of_arguments}"
                )
            return func(*args, **kwargs)

        return guard_arguments

    return count_guard
