# Given a tuple of numbers, return a new tuple containing only the prime numbers.


def is_prime(number):
    is_prime_numbere = True
    if number >= 2 :
        for i in range(2, number):
            if number % i == 0:
                is_prime_numbere =  False
                break
        return is_prime_numbere
    else:
        is_prime_numbere = False
        return is_prime_numbere


def prime_tuple(my_tuble):
    list_a = []
    for item in my_tuble:
        if(is_prime(item)):
            list_a.append(item)
    return tuple(list_a)



tuple_a = tuple(range(1, 100))

result = prime_tuple(tuple_a)
print(result)



# (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)