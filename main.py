import sys
from stats import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = get_num_words(sys.argv[1])
    occurence_count_of_characters = get_occurence_count_of_characters(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in get_sorted_occurence_count_of_characters(occurence_count_of_characters):
        print(f'{char_dict["char"]}: {char_dict["num"]}')
    print("============= END ===============")

main()
