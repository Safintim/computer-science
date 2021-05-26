def count_primes(n: int) -> int:
    if n <= 2:
        return 0

    numbers = {}
    for i in range(2, int(n ** 0.5) + 1):
        if i not in numbers:
            for j in range(i * i, n, i):
                numbers[j] = False
    return n - len(numbers) - 2
