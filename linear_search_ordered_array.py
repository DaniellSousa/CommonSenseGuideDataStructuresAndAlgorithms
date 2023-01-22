list_ordered_array = [3, 17, 75, 80, 202]


def linear_search(array, search_value):
    print("Searching for: " + str(search_value))
    for index, element in enumerate(array):
        if element == search_value:
            return index
        elif element > search_value:
            break

    return None


index_value = linear_search(list_ordered_array, 80)
print("index: " + str(index_value))
