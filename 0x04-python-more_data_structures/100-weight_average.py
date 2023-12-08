#!/usr/bin/python3

def calculate_weighted_average_another_form(data):
    if not data:
        return 0

    numerator = sum(map(lambda x: x[0] * x[1], data))
    denominator = sum(map(lambda x: x[1], data))

    return numerator / denominator
