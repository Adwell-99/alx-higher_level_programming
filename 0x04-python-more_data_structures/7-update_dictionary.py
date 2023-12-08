#!/usr/bin/python3 
def modify_dictionary(dictionary, key, value):
    updated_dict = dictionary.copy()
    updated_dict[key] = value
    return updated_dict
