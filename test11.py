# Write a function that takes a tuple of strings and returns a tuple with the length of each string.


def len_of_stiring_tup(my_tuple):
    len_tuple = []
    for word in my_tuple:
        len_tuple.append(len(word))
    return tuple(len_tuple)




fruits = ("apple", "bananna", "graps", "pappay", "watermelon", "guava", "pinneapple")

result = len_of_stiring_tup(fruits)

print(result)


# (5, 7, 5, 6, 10, 5, 10)