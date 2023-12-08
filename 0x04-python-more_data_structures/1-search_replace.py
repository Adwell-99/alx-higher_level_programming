#!/usr/bin/python3

def alternative_search_replace(my_list, search, replace):
    # Check whether the list is empty
    if not my_list:
        return []

    # Use a list comprehension with a conditional expression to replace elements
    new_list = [replace if item == search else item for item in my_list]

    return new_list
