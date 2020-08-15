vowels = ['a', 'e', 'i', 'o', 'u']

word = input('provide a word to search for vowels: ')
found = {}

for letter in word:
    if letter in vowels:
        found[letter] = found[letter] + 1 if letter in found else 1

for k, v in sorted(found.items()):
    print(k, 'was found:', v, 'time(s)')
