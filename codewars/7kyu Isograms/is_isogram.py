def is_isogram(string):
    # len(string) == len(set(string.lower()))
    lower_string = string.lower()
    repeat_chars = filter(lambda ch: lower_string.count(ch) > 1, lower_string)
    return len(list(repeat_chars)) == 0
