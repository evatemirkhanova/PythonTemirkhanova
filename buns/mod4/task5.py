file_name = input("Введите имя файла: ")

statistics = {}                                               # СОЗДАДИМ ПУСТОЙ СЛОВАРЬ, В КОТОРОМ БУДЕМ ХРАНИТЬ СТАТИСТИКУ ПО БУКВАМ

with open(file_name, "r") as file:                            # СЧИТЫВАЕМ ФАЙЛ ПОСИМВОЛЬНО
    for line in file:
        for char in line:
            if char.isalpha():                                # ПРОВЕРКА: ВЫБРАННЫЙ СИМВОЛ - БУКВА?
                if char in statistics:                        # ПРОВЕРКА: ВСТРЕЧАЛСЯ ЛИ ЭТОТ СИМВОЛ РАНЕЕ В СЛОВАРЕ statistics
                    statistics[char] += 1                     # ЕСЛИ ДА, ТО УВЕЛИЧИВАЕМ СЧЕТЧИК НА 1
                else:
                    statistics[char] = 1                      # ЕСЛИ НЕТ, ТО ДОБАВЛЯЕМ НОВУЮ ПАРУ КЛЮЧ-ЗНАЧЕНИЕ СО ЗНАЧЕНИЕМ 1

# ПОСЛЕ ПОДСЧЕТА СТАТИСТИКИ, НУЖНО ОТСОРТИРОВАТЬ ЕЕ ПО ЧАСТОТЕ ВСТРЕЧАЕМОСТИ БУКВ:

sorted_stat = sorted(statistics, key=lambda x: statistics[x]) # ФУНКЦИЯ key УКАЗЫВАЕТ, ПО КАКОМУ ЗНАЧЕНИЮ НУЖНО СОРТИРОВАТЬ

output_file_name = "output.txt"                               # СОЗДАДИМ НОВЫЙ ФАЙЛ ДЛЯ ВЫВОДА РЕЗУЛЬТАТА В НЕГО

with open(output_file_name, "w") as output_file:              # ЗАПИШЕМ В ЭТОТ ФАЙЛ ОТСОРТИРОВАННУЮ СТАТИСТИКУ, ИСПОЛЬЗУЯ ЦИКЛ
    for char in sorted_stat:
        output_file.write(f"{char}: {statistics[char]}\n")
