# Write a function that takes a sentence and returns a dictionary with word frequency counts (case-insensitive).


def word_frequ(my_sentance):

    freq_dict = {}

    formated = my_sentance.lower().strip()
    for word in formated.split(" "):
        freq_dict[word] = formated.count(word)
    return freq_dict


# sent = "apple banana apple orange banana apple"
sent = "Apple apple APPLE banana BANANA banana grape "

print(word_frequ(sent))


# {'apple': 3, 'banana': 3, 'grape': 1}