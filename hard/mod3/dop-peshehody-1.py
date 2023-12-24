import json
import re

"""
Функция description_format принимает строку inform в качестве аргумента. 
Затем она разбивает эту строку на отдельные части, используя разделитель ". ". 
Затем каждая часть преобразуется в нижний регистр с помощью метода lower(), а затем в заглавную с помощью метода capitalize(). 
В конце строки соединяются с помощью метода join(), а затем все точки заменяются на ". " с помощью метода replace(). 

"""
def description_format(inform: str):
    parts = inform.split(". ")
    for i in range(len(parts)):
        parts[i] = parts[i].lower()
        parts[i] = parts[i].capitalize()

    return '.'.join(parts).replace('.', '. ')


"""
Функция description_salary принимает строку inform в качестве аргумента, 
преобразует ее в число с помощью метода float(), 
форматирует число с помощью метода format() 
(в данном случае ограничивает количество цифр после запятой до 3) и возвращает результат.
"""

def description_salary(inform: str):
    return "{:.3f}".format(float(inform))


"""
Функция description_key_phrase принимает строку inform в качестве аргумента. 
Сначала она преобразует строку в верхний регистр с помощью метода upper(), 
затем добавляет восклицательный знак в конец строки. Затем результат возвращается.
"""

def description_key_phrase(inform: str):
    temp = inform.upper() + '!'
    return temp[::]

"""
Функция description_addition принимает строку inform в качестве аргумента. 
Сначала она преобразует строку в нижний регистр с помощью метода lower(). 
Затем к результату добавляются троеточия в начале и в конце строки. 
Затем результат возвращается.
"""

def description_addition(inform: str):
    temp = inform.lower()
    return '...' + temp[::] + '...'

"""
Функция description_reverse принимает строку inform в качестве аргумента. 
С помощью среза [::-1] она обращает строку в обратном порядке и возвращает результат
"""

def description_reverse(inform: str):
    return inform[::-1]

"""
Функция description_company_info принимает строку inform в качестве аргумента. 
Она использует модуль re для выполнения регулярного выражения и удаления всех круглых скобок
и их содержимого из строки. Затем результат возвращается.
"""

def description_company_info(inform: str):
    result = re.sub(r'\([^()]*\)', '', inform)
    result = re.sub(r'\([^)]*\)', '', result)
    return result


"""
Функция description_key_skills принимает строку inform в качестве аргумента. 
Она использует метод replace() для замены всех вхождений ' ' на пробел ' '. Затем результат возвращается.
"""

def description_key_skills(inform: str):
    result = inform.replace(' ', ' ')
    return result


# Вводится две строки: text и headings, которые используются далее в коде.
text = input()
headings = input()

"""
Строка text разбивается на части, используя разделитель ;, и сохраняется в списке temp. 
Затем создается пустой словарь result. 
В цикле происходит разделение каждой части на ключ и значение, используя разделитель :. 
Ключ очищается от пробелов и сохраняется в переменной key. Если ключ содержится в строке headings, 
то вложенным циклом происходит формирование значения для этого ключа путем конкатенации всех остальных частей. 
Результат записывается в словарь result.
"""

temp = text.split(';')
result = {}
for i in temp:
    information = i.split(':')
    key = information[0].replace(' ', '')
    if key in headings:
        for j in range(1, len(information)):
            result[key] = result.get(key, '') + information[j]

"""
В цикле происходит обработка значений в словаре result. 
Первым делом удаляется первый символ у значения value, чтобы удалить лишний пробел, 
который добавляется при формировании значения. Затем в зависимости от ключа значения, 
вызывается соответствующая функция для обработки значения. 
Полученный результат записывается обратно в словарь result.
"""

for key, value in result.items():
    value = value[1::]
    if key == 'description':
        result[key] = description_format(value)
    elif key == 'salary':
        result[key] = description_salary(value)
    elif key == 'key_phrase':
        result[key] = description_key_phrase(value)
    elif key == 'addition':
        result[key] = description_addition(value)
    elif key == 'reverse':
        result[key] = description_reverse(value)
    elif key == 'company_info':
        result[key] = description_company_info(value)
    elif key == 'key_skills':
        result[key] = description_key_skills(value)

"""
Словарь result преобразуется в JSON формат с помощью метода dumps() из модуля json. Затем результат выводится на экран с помощью функции print().
"""

json_output = json.dumps(result)
print(json_output)