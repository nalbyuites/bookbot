def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(book):
    book_word_list = len(get_book_text(book).split())
    return book_word_list

def get_word_list(book):
    return get_book_text(book).split()

def get_occurence_count_of_characters(book):
    occurence_dict = {}
    for word in get_word_list(book):
        # lower-casing since we don't want character duplicates
        word_lower_case = word.lower()
        # looping over characters of each word string
        for char in word_lower_case:
            # incrementing the current character occurence count if present as dict key, else setting to 0
            if char in occurence_dict:
                char_count = occurence_dict[char]
                char_count += 1
            else:
                char_count = 1
            # setting the dict value to the new character count
            occurence_dict[char] = char_count
    return occurence_dict

def sort_on(items):
    return items["num"]

def get_sorted_occurence_count_of_characters(occurence_dict):
    # Instantiate an empty list consisting of character dictionaries.
    occurence_list = []
    for char in occurence_dict:
        # Instantiate an empty dictionary for each character. for eg., {"char": "b", "num": 4868}
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = occurence_dict[char]
        occurence_list.append(char_dict)
    occurence_list.sort(reverse=True, key=sort_on)
    return occurence_list
