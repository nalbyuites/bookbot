from stats import *

def main():
    num_words = get_num_words("books/frankenstein.txt")
    occurence_count_of_characters = get_occurence_count_of_characters("books/frankenstein.txt")

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char_dict in get_sorted_occurence_count_of_characters(occurence_count_of_characters):
        print(f'{char_dict["char"]}: {char_dict["num"]}')
    print(f"============= END ===============")

main()
