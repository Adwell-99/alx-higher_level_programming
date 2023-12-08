#!/usr/bin/python3
def remove_key(dictionary, key=""):
    updated_dict = {k: v for k, v in dictionary.items() if k != key}
    return updated_dict
