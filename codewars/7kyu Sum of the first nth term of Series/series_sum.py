def series_sum(n):
    num = 1
    denom = 1
    s = sum(num / (denom + (i * 3)) for i in range(n))
    return '{:.2f}'.format(s)
