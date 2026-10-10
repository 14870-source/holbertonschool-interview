#!/usr/bin/python3
"""Calculate the minimum number of operations to obtain n H characters."""


def minOperations(n):
    """Return the minimum operations needed to obtain n H characters."""
    if not isinstance(n, int) or isinstance(n, bool) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
