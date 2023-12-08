#!/usr/bin/python3
from functools import reduce

def find_top_score(dictionary):
    if not dictionary:
        return None

    return reduce(lambda x, y: x if dictionary[x] > dictionary[y] else y, dictionary)
