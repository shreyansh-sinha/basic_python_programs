def max_difference(a, b, c):
    #docstring
    """ Returns the maximum difference between any two numbers among a, b, c
    >>> max_difference(1, 5, -5)
    10
    """

    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(c-a)

    return max(diff1, diff2, diff3)

help(max_difference)
print(max_difference(1, 5, -5))
