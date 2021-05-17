def square_digits(num):
    return int(''.join(map(lambda ch: str(int(ch) ** 2), str(num))))