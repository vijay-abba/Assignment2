# Remove all duplicates from a list [1, 2, 2, 3, 4, 4, 5].


def remove_dublicates(my_list):
    return list(set(my_list))


print(remove_dublicates([1, 2, 2, 3, 4, 4, 5]))