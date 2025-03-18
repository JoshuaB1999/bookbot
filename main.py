import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

from stats import num_words
from stats import num_of_letters

def print_report(path, word_count, char_list):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}...")
    print ("------------ Word Count ------------")
    print (f"Found {word_count} total words")
    print ("------------ Character Count ------------")
    for entry in char_list:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['count']}")
    print ("============ END =============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num = num_words(text)
    number_of_letters = num_of_letters(text)
    sorted_chars = num_of_letters(text)
    print_report(sys.argv[1], num, sorted_chars)

main()
