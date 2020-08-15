def search_for_vowels(word):
    """Returns True when the word contains a vowel. Otherwise, returns False"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))

    for vowel in found:
        print(vowel)

    return bool(found)


print(search_for_vowels('francisco'))
print(search_for_vowels('sky'))
