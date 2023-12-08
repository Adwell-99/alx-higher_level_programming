#!/usr/bin/python3
def calculate_weighted_average(another_list=[]):
    if not another_list:
        return 0

    total_score, total_weight = 0, 0

    for score, weight in another_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight
