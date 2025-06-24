import sys
from stats import count_words
from stats import count_characters
from stats import sort


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    text = get_book_text(filepath)
    words = count_words(text)
    characters = count_characters(text)
    sorted = sort(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for item in sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


main()
