def is_palindrome(word):
    """
        Prints whether a word or sentence is a palindrome, based on argument passed
        Argument:
        word
    """
    lower_word = word.lower()
    replaced_word = lower_word.replace(" ", "")
    if replaced_word != replaced_word[::-1]:
        return f"{word.capitalize()} is not a palindrome."
    else:
        return f"{word.capitalize()} is a palindrome."


print(is_palindrome("Anna"))
print(is_palindrome("potop"))
print(is_palindrome("bootcamp"))
print(is_palindrome("A to kiwi zdziwi kota"))