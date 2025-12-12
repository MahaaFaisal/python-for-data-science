

def ft_filter(function, object):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable\
    for which function(item)\
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return iter([item for item in object if item])
    else:
        return iter([item for item in object if function(item)])
