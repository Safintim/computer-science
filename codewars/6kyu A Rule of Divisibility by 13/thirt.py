def get_10_mod_13(n):
    return [(10 ** i) % 13 for i in range(n)]


def thirt(number):
    str_number = str(number)
    mods = get_10_mod_13(len(str_number))
    total = sum(int(num) * mod for num, mod in zip(reversed(str_number), mods))
    
    if number == total:
        return number
    return thirt(total)