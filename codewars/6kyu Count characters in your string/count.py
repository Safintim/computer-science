import collections


def count(string):
    return dict(collections.Counter(string))
