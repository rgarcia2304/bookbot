def get_book_word_count(book_string):
    count = 0
    split_book_string = book_string.split(" ")

    for i in split_book_string:
        count += 1
    
    return count

def count_frequency(book_string):
    count_dict = {}

    for char in book_string:
        test_char = char.lower()
        if test_char in count_dict:
            count_dict[test_char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def get_value(d):
    return list(d.values())[0]

def format_count(char_dict):
    lst_of_char_info = []
    
    for key in char_dict:
        new_dict ={}
        new_dict[key] = char_dict[key]
        #new_dict = dict(key = char_dict[key])
        lst_of_char_info.append(new_dict)

    lst_of_char_info.sort(reverse=True, key=get_value)
    
    return lst_of_char_info


