#!/usr/bin/python3
def remove_keys_with_value(input_dict, value):
    return {key: val for key, val in input_dict.items() if val != value}
