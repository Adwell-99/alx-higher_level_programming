def find_unique_elements(set_1, set_2):
    unique_elements_set = set()

    # Add elements from set_1 that are not in set_2
    unique_elements_set.update(element for element in set_1 if element not in set_2)
    
    # Add elements from set_2 that are not in set_1
    unique_elements_set.update(element for element in set_2 if element not in set_1)

    return unique_elements_set
