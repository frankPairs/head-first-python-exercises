def search_for_vowels(phrase: str) -> set:
    """Returns any vowels found in a supplied word"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letters: str) -> set:
    """Returns any letters found in a supplied phrase"""
    return set(letters).intersection(set(phrase))

