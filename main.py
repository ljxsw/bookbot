from stats import count_words
from stats import count_characters
from stats import sort


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    characters = count_characters(text)

    sort(characters)


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


main()
