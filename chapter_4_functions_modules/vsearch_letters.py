def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Returns any letters found in a supplied phrase"""
    return set(letters).intersection(set(phrase))


print(search_for_letters('hello world', 'hw'))
print(search_for_letters(letters='lth', phrase='learning python'))
print(search_for_letters('francisco'))
print(search_for_letters(phrase='sky'))
