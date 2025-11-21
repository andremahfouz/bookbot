from stats import count_words, count_char, sorted_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

sorted_char_list = []
dict_char = count_char(filepath)
sorted_char_list = sorted_list(dict_char)
new_list = []
for item in sorted_char_list:
    if item["char"].isalpha():
        new_list.append(item)
    else:
        continue

new_list_string = str()
for item in new_list:
    new_list_string += f"{item["char"]}: {item["num"]}\n"
new_list_string = new_list_string.rstrip("\n")

print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
---------- Word Count ----------
Found {count_words(filepath)} total words
--------- Character Count -------
{new_list_string}
============= END ===============
""")
