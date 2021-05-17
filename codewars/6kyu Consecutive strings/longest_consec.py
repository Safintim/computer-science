def longest_consec(strings, k):
    len_strings = len(strings)
    longest_str = ''
    if not strings or k <= 0 or k > len_strings:
        return longest_str

    for current_index, current in enumerate(strings):
        new_str = ''.join(s for s in strings[current_index:current_index + k])
        if len(new_str) > len(longest_str):
            longest_str = new_str
    return longest_str
