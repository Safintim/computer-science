def binary_array_to_number(arr):
    bin_string = ''.join(str(el) for el in arr)
    return int(bin_string, 2)