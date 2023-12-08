#!/usr/bin/python3

def count_keys(dictionary):
    count = sum(1 for _ in dictionary.keys())
    return count
