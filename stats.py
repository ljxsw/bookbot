def count_words(text):
    word_count = 0
    words = text.split()

    for word in words:
        word_count += 1

    return word_count


def count_characters(text):
    count = {}

    for s in text:
        s = s.lower()
        if s not in count:
            count[s] = 1
        else:
            count[s] += 1

    return count


def sort_on(dictionary):
    return dictionary["num"]


def sort(dictionary):
    sorted = []

    for key in dictionary:
        new_dict = {"char": key, "num": dictionary[key]}
        sorted.append(new_dict)

    sorted.sort(reverse=True, key=sort_on)

    return sorted
