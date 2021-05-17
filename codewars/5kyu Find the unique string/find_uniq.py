def find_uniq(arr):
    char_sets = list(map(lambda x: set(x.lower().replace(' ', '')), arr))
    
    first = char_sets[0]
    if char_sets.count(first) > 1:
        pattern = first
    else:
        return arr[0]
    
    for index, s in enumerate(char_sets):
        if pattern != s:
            return arr[index]
        