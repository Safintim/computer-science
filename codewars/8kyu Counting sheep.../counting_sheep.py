def count_sheeps(sheeps):
    # sheeps.count(True)
    return len(list(filter(lambda sheep: sheep is True, sheeps)))