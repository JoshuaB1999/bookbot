def num_words(text):
    num = 0
    words = text.split()
    for word in words:
        num += 1
    return num

def sort_on(dict):
    return dict["count"]

def num_of_letters(string):
    new_string = string.lower()
    dictionary = {}
    new_dict = []
    for letter in new_string:
        if not letter.isalpha():
            continue
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    new_dict = sorter(dictionary)
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict

def sorter(dictionary):
    sorted_list = []
    for char, count in dictionary.items():
        sorted_list.append({"char": char, "count": count})
    return sorted_list
