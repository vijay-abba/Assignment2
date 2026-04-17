# Find the second largest number in a list without sorting


def second_laregest(my_list):
    largest = my_list[0]
    sec_laregest = my_list[0]
    for num in my_list:
        if num > largest:
            largest = num

    for number in my_list:
        if number < largest and number > sec_laregest:
            sec_laregest = number
    
    return sec_laregest


print(second_laregest([23, 45, 12, 67, 89, 34]))