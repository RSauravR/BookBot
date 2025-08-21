import sys
from stats import get_total_word_count
from stats import character_appearing_calculator
from stats import sorted_character_appearing_calculator
from book_text import get_books_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    books_text = get_books_text(path)
    books_text = get_books_text(path)
    total_word_count = get_total_word_count(books_text)
    char_dict = character_appearing_calculator(books_text)
    sorted_char_list = sorted_character_appearing_calculator(char_dict)
    print_report(sorted_char_list, path, total_word_count)

def print_report(sorted_char_list, path, total_word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_list:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['count']}")
    print("============= END ===============")

main()