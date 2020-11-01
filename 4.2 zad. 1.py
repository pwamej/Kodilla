def is_palindrome(word):
    """
        Prints whether a word is a palindrome, based on argument passed
        Argument:
        word
    """
    word = word.lower()
    word_len = len(word)
    for index in range(word_len):
        if word[index] != word[-index-1]:
            return f"{word.capitalize()} is not a palindrome."
    return f"{word.capitalize()} is a palindrome."


print(is_palindrome("Anna"))
print(is_palindrome("potop"))
print(is_palindrome("bootcamp"))