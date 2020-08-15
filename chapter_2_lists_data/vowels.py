vowels = ['a', 'e', 'i', 'o', 'u']

word = input('provide a word to search for vowels: ')
found = []

for letter in word:
    if letter in vowels and letter not in found:
        found.append(letter)

print(found)