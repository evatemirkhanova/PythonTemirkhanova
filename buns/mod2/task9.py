string = input()
vowels_count = 0
consonants_count = 0

vowels = 'яюэыуоиёеа'
consonants = 'бвгджзйклмнпрстфхцчшщ'

for i in range(len(string)):
    if string[i] in vowels:
        vowels_count += 1
    elif string[i] in consonants:
        consonants_count += 1
print(vowels_count, consonants_count)