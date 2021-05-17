def disemvowel(string):
    vowels = 'aeiou'
    return ''.join(filter(lambda ch: ch.lower() not in vowels, string))