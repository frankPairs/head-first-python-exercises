def search_for_vowels(word):
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))

    for vowel in found:
        print(vowel)


search_for_vowels('francisco')
