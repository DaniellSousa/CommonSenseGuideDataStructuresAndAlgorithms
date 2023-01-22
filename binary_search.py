list_ordered_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(array, search_value):
    print("Looking for " + str(search_value))
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = int((upper_bound + lower_bound) / 2)
        value_at_midpoint = array[midpoint]

        if search_value == value_at_midpoint:
            return midpoint
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1

    return None


value = 8
index_value = binary_search(list_ordered_array, value)
print("Index: " + str(index_value))
