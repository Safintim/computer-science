import collections


def duplicate_count(text):
    counter = collections.Counter(text.lower())
    return len(list(filter(lambda item: item[1] > 1, counter.items())))
     