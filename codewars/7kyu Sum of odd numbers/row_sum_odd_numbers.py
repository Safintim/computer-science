def row_sum_odd_numbers(n):
    triangle = []

    def generator_odd():
        current = 1
        while True:
            if current % 2 == 1:
                yield current
            current += 1

    get_odd = generator_odd()
    for i in range(1, n + 1):
        row = []
        while len(row) < i:
            row.append(next(get_odd))
        triangle.append(row)

    return sum(triangle[n-1])
