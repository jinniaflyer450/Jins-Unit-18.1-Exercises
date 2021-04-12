def print_upper_words(words, must_start_with):
    """Given a list of words and required first letters, prints each word that starts with a required first letter in uppercase."""
    for word in words:
        for char in must_start_with:
            if word.startswith(char):
                print(word.upper())
            else:
                continue 

