from stats import count_words


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)

    print(f"{count_words(text)} words found in the document")


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


main()
