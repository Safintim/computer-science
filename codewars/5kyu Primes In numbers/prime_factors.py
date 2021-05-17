import collections


def prime_factors(n):
    dividers = collections.Counter()
    div = 2

    while div * div <= n:
        if n % div == 0:
            dividers[div] += 1
            n //= div
        else:
            div += 1

    if n > 1:
        dividers[n] += 1

    return ''.join(
        f'({key}**{value})' if value > 1 else f'({key})'
        for key, value in dividers.items()
    )
