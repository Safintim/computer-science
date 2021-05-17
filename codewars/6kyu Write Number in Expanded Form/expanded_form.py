def expanded_form(num):
    a = []
    div = 1
    while num > 0:
        last_num = num % 10
        if last_num != 0:
            a.append(last_num * div)
        div *= 10
        num //= 10
    return ' + '.join(map(lambda x: str(x), reversed(a)))