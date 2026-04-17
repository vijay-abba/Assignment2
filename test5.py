# Given two lists, create a third list that contains only the common elements (intersection). 

# print({1, 2, 3, 3, 4}.intersection({2, 3, 5, 6}))


def list_intersection(list_one, list_two):
    common = set(list_one).intersection(set(list_two))
    return list(common)


list_a = [1, 2, 3, 3, 4]
list_b = [2, 3, 5, 6]
print(list_intersection(list_a, list_b))