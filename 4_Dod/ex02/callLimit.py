
def callLimit(limit: int):
    """Return a decorator that limits how many times a function can be called."""
    count = 0

    def callLimiter(function):
        """Wrap a function with a shared call counter."""

        def limit_function(*args, **kwds):
            """Call the wrapped function until the configured limit is reached."""
            nonlocal count
            if (count < limit):
                count += 1
                return function(*args, **kwds)
            print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
