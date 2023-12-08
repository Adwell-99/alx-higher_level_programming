i#!/usr/bin/python3

def display_sorted_dictionary(dictionary):
    for key, value in sorted(dictionary.items()):
        print("{}: {}".format(key, value))
