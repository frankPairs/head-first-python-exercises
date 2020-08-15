def search_for_vowels(word: str) -> set:
    """Returns any vowels found in a supplied word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


print(search_for_vowels("francisco"))
print(search_for_vowels("sky"))
