import json
import re

text = input()
headings = input()

text = text[:len(text)-1]

s1_list = text.split(";")
s2_list = headings.split(",")

for i in range(len(s1_list)):
    s1_list[i] = s1_list[i].strip()

for i in range(len(s2_list)):
    s2_list[i] = s2_list[i].strip()

# Определение функции для форматирования описания
def Description(s: str) -> str:
    # Разделение описания на предложения
    s_list = s.split(". ")
    
    # Инициализация новой строки для форматированного описания
    s_new = ""
    for i in range(len(s_list)): # Итерация по s_list
        s_list[i] = s_list[i].lower() # Преобразование каждого предложения в нижний регистр
        
        a = s_list[i][0]
        a= a.upper() # Первая буква каждого предложения в верхний регистр
        s_list[i] = a + s_list[i][1:]

        # Если это не последнее предложение
        if i != len(s_list) - 1:
            # Добавление отформатированного предложения, за которым следует точка и пробел
            s_new += s_list[i] + ". "
        
        # Добавление последнего отформатированного предложения без точки и пробела    
        else:
            s_new += s_list[i]
    # Возврат отформатированного описания
    return s_new

# Определение функции для форматирования заработной платы
def Salary(num: float) -> str:
    return format(round(num, 3), '.3f')

# Определение функции для форматирования ключевой фразы
def Key_phrase(s: str) -> str:
    return s.upper() + '!'

# Определение функции для добавления текста
def Addition(s: str) -> str:
    return '...' + s.lower() + '...'

# Определение функции для разворота текста
def Reverse(s: str) -> str:
    return "".join(reversed(s))

# Определение функции для извлечения информации о компании
def Company_info(s: str) -> str:
    c = 0
    s_new = ""
    for i in range(len(s)):
        if s[i] == '(':
            c+=1
        if c==0:
            s_new += s[i]
        if s[i] == ')':
            c-=1
    
    return s_new

# Определение функции для форматирования ключевых навыков
def Key_skills(s: str) -> str:
    return s.replace("&nbsp", " ")

d = dict()

for i in range(len(s1_list)):
    l = s1_list[i].split(": ")
    d[l[0]] = l[1]

d_result = dict()

for i in range(len(s2_list)):  # Итерация по s2_list
    if s2_list[i] in d.keys():  # Если заголовок присутствует в ключах словаря
        if s2_list[i] == "description":  # Если заголовок - "description"
            d_result[s2_list[i]] = Description(d[s2_list[i]])  # Добавление отформатированного описания в результаты
        elif s2_list[i] == "salary":  # Если заголовок - "salary"
            d_result[s2_list[i]] = Salary(float(d[s2_list[i]]))  # Добавление отформатированной заработной платы в результаты
        elif s2_list[i] == "key_phrase":  # Если заголовок - "key_phrase"
            d_result[s2_list[i]] = Key_phrase(d[s2_list[i]])  # Добавление отформатированной ключевой фразы в результаты
        elif s2_list[i] == "addition":  # Если заголовок - "addition"
            d_result[s2_list[i]] = Addition(d[s2_list[i]])  # Добавление отформатированного дополнения в результаты
        elif s2_list[i] == "reverse":  # Если заголовок - "reverse"
            d_result[s2_list[i]] = Reverse(d[s2_list[i]])  # Добавление развернутого текста в результаты
        elif s2_list[i] == "company_info":  # Если заголовок - "company_info"
            d_result[s2_list[i]] = Company_info(d[s2_list[i]])  # Добавление извлеченной информации о компании в результаты
        elif s2_list[i] == "key_skills":  # Если заголовок - "key_skills"
            d_result[s2_list[i]] = Key_skills(d[s2_list[i]])  # Добавление отформатированных ключевых навыков в результаты

# Преобразование словаря результатов в строку JSON
result = json.dumps(d_result)

print(result)