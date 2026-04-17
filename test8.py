# Count how many times the number 5 appears in (1, 5, 3, 5, 7, 5, 9).

def count_number(my_iter, number):
    return my_iter.count(number)

tuple_1 = (1, 5, 3, 5, 7, 5, 9)
print(count_number(tuple_1, 5))
