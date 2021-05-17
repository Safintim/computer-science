def iq_test(string_numbers):
    numbers = list(map(lambda ch: int(ch), string_numbers.split()))
    even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
    
    if len(even_numbers) > 1:
        remainder = 1
    else:
        remainder = 0
    
    for index, num in enumerate(numbers, start=1):
        if num % 2 == remainder:
            return index
