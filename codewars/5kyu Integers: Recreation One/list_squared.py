import math


def get_sum_squared_divisors(number):
    end = int(math.sqrt(number)) + 1
    for div in range(1, end):
        if number % div == 0:
            yield div ** 2
            if number / div != div:
                yield (number / div) ** 2


def is_square(n):
    return math.sqrt(n) % 1 == 0


def list_squared(m, n):
    squared = []
    for num in range(m, n + 1):
        sum_divisors = sum(get_sum_squared_divisors(num))
        if is_square(sum_divisors):
            squared.append([num, sum_divisors])
    return squared
