# Find the largest and smallest number in a list [23, 45, 12, 67, 89, 34] without using max() or min().

my_list_a = [23, 45, 12, 67, 89, 34]

def find_min_and_max(my_list):
    smallest = my_list[0]
    largest  = my_list[0]
    for number in my_list:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    return f"Smallest: {smallest}, Largest: {largest}"


result = find_min_and_max(my_list_a)
print(result)


# OUTPUT
# Smallest: 12, Largest: 89