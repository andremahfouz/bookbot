def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(filepath):
    word_list = []
    word_string = get_book_text(filepath)
    word_list = word_string.split()
    num_words = len(word_list)
    return num_words

def count_char(filepath):
    char_list = []
    word_string = get_book_text(filepath)
    char_list = list(word_string.lower())
    char_dict = {}
    for char in char_list:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] +=1
    return char_dict

def sorted_list(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        new_dict = {"char": key, "num": value}
        dict_list.append(new_dict)
    def sort_on(items):
        return items["num"]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
