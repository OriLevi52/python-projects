def find_longest_word(l):
    max_len = 0
    longest_words = []

    for word in l:
        if len(word) > max_len:
            longest_words = [word]
            max_len = len(word)
        elif len(word) == max_len:
            longest_words.append(word)

    return longest_words


