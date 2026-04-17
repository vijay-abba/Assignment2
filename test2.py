# Write a program to count how many even and odd numbers are in a list. 

def find_even_and_odd_count(my_list):

    even_numbers = []
    odd_numbers = []

    for number in my_list:
        even_numbers.append(number) if number % 2 == 0 else odd_numbers.append(number)

    return f"In the given list {my_list} there are {len(even_numbers)} Even, and {len(odd_numbers)} Odd numbers"

list_a = [1, 2, 3, 4, 5, 6]
list_b = [10, 15, 20, 25, 30]
list_c = [7, 9, 11, 13]
list_d = [2, 4, 6, 8, 10, 12]
list_e = [0, 1, 2, 3, 4]
list_f = [-1, -2, -3, -4, -5]
list_g = [21, 22, 23, 24, 25, 26, 27]
list_h = [100]
list_i = [101]
list_j = []


print(find_even_and_odd_count(list_a))
print(find_even_and_odd_count(list_b))
print(find_even_and_odd_count(list_c))
print(find_even_and_odd_count(list_d))
print(find_even_and_odd_count(list_e))
print(find_even_and_odd_count(list_f))
print(find_even_and_odd_count(list_g))
print(find_even_and_odd_count(list_h))
print(find_even_and_odd_count(list_i))
print(find_even_and_odd_count(list_j))



# OUTPUT
"""
In the given list [1, 2, 3, 4, 5, 6] there are 3 Even, and 3 Odd numbers
In the given list [10, 15, 20, 25, 30] there are 3 Even, and 2 Odd numbers
In the given list [7, 9, 11, 13] there are 0 Even, and 4 Odd numbers
In the given list [2, 4, 6, 8, 10, 12] there are 6 Even, and 0 Odd numbers
In the given list [0, 1, 2, 3, 4] there are 3 Even, and 2 Odd numbers
In the given list [-1, -2, -3, -4, -5] there are 2 Even, and 3 Odd numbers
In the given list [21, 22, 23, 24, 25, 26, 27] there are 3 Even, and 4 Odd numbers
In the given list [100] there are 1 Even, and 0 Odd numbers
In the given list [101] there are 0 Even, and 1 Odd numbers
In the given list [] there are 0 Even, and 0 Odd numbers
"""