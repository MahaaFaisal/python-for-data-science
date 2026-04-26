
def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        nonlocal count, limit
        def limit_function(*args, **kwds):
            nonlocal count, limit
            if count < limit:
                count += 1
                function (*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter

@callLimit(3)
def f():
    print ("f()")


@callLimit(1)
def g():
    print ("g()")


for i in range(3):
    f()
    g()
