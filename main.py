from stats import get_num_words, get_chars_dict, sort_chars_by_count
import sys

def get_book_text(filepath):
    # Open the file at the given filepath in read mode
    with open(filepath, "r") as file:
        # Read the entire contents of the file
        content = file.read()
    # Return the contents as a string
    return content

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    # Get the contents of the frankenstein.txt file
    book_contents = get_book_text(sys.argv[1])

    word_count = get_num_words(book_contents)

    char_frequency = get_chars_dict(book_contents)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    sorted_char_frequency = sort_chars_by_count(char_frequency)
    for item in sorted_char_frequency:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
