def create_palindrome(word):
    characters = []
    character_count = {}

    # Заполнение списка символов и подсчет повторений каждого символа
    for char in word:
        if char in characters:
            character_count[char] += 1
        else:
            characters.append(char)
            character_count[char] = 1

    # ПРОВЕРКА
    #print('список символов')
    #print(characters)
    #print('подсчет повторений каждого символа')
    #print(character_count)

    # Создание палиндрома
    palindrome = ""
    center_character = ""

    for char in characters:
        count = character_count[char]
        if count % 2 == 0:                    # ЕСЛИ СИМВОЛА ЧЕТНОЕ КОЛ-ВО
            palindrome += char * (count // 2) # БУДЕМ ИМ ЗАПОЛНЯТЬ 1-УЮ ПОЛОВИНУ ПОЛИНДРОМА
            character_count[char] = 0         # ТОБЫ БУКВЫ НЕ ПОВТОРЯЛИСЬ - УДАЛЯЕМ ИХ, КАК "ИСПОЛЬЗОВАННЫЕ" 
        elif center_character == "":          # ЕСЛИ СИМВОЛ ПОВТОРЯЕТСЯ НЕЧЕТНОЕ КОЛ-ВО РАЗ И В ЦЕНТРЕ ЕЩЕ НЕТ НИЧЕГО
            center_character = char * count   # ТО СТРОКА, СОСТОЯЩАЯ ТОЛЬКО ИЗ НЕГО, ЕГО КОЛ-ВО РАЗ, СТАНЕТ ЦЕНТРАЛЬНОЙ
        else:
            print("Невозможно создать палиндром")
            return None

    palindrome += center_character + palindrome[::-1]
    return palindrome


# Получение входного слова от пользователя
word = input("Введите слово: ")

# Создание палиндрома из введенного слова
result = create_palindrome(word)

if result:
    print("Палиндром:", result)

