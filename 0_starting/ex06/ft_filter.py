def ft_filter(condition, words):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if condition is None:
        return [word for word in words if word]
    return [word for word in words if condition(word)]
