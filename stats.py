def count_words(text):
    word_count = 0
    words = text.split()

    for word in words:
        word_count += 1

    return word_count
