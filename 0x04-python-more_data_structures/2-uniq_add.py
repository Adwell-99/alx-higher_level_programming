#!/usr/bin/python3

def unique_sum_alternative(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return 0

    # Use the sum function along with a set comprehension to calculate the sum of unique elements
    return sum({x for x in my_list})

