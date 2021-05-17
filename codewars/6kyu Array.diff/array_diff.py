def array_diff(arr1, arr2):
    return list(filter(lambda x: x not in arr2, arr1))
