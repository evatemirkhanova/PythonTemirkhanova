import json
from bs4 import BeautifulSoup
import requests

# Объявление словаря для обменного курса валют
exchange = {
    '₽': 1.0,
    '$': 100.0,
    '€': 105.0,
    '₸': 0.210,
    'Br': 30.0,
}

html = input()  # Ввод имени HTML-файла

with open(html) as file:
    soup = BeautifulSoup(file, "html.parser")

    # Извлечение данных из HTML-файла
    vacancy = soup.find('h1', attrs={'data-qa': 'vacancy-title'}).text
    salary = soup.find('div', attrs={'data-qa': 'vacancy-salary'}).text
    experience = soup.find('p', attrs={'class': 'vacancy-description-list-item'}).text
    company = soup.find('span', attrs={'class': 'vacancy-company-name'}).text
    description = soup.find('div', attrs={'data-qa': 'vacancy-description'}).text
    skills = [i.text for i in soup.find_all('div', attrs={'data-qa': 'bloko-tag bloko-tag_inline skills-element'})]
    created_at = soup.find('p', attrs={'class': 'vacancy-creation-time-redesigned'}).text

    d = dict()  # Создание пустого словаря

    validate_digit = '0123456789₽$€₸Br'  # Строка для валидации цифр и символов валют

    # Приведение к корректному выводу vacancy
    d["vacancy"] = vacancy

    # Приведение к корректному выводу salary
    salary_str = ''.join([i for i in salary if i in validate_digit])
    for i in range(len(salary_str)):
        if salary_str[i] == '0' and salary_str[i+1] != '0' and salary_str[i+1] not in exchange.keys():
            break

    salary_str = salary_str[:i+1] + '-' + salary_str[i+1:]
    salary_list = ' '.join(salary_str.split('-')).strip().split(' ')

    if len(salary_list) > 1:
        if salary_list[1][len(salary_list[1])-2:] != 'Br':
            salary_list[0] = int(salary_list[0]) * exchange[salary_list[1][-1]]
            salary_list[1] = int(salary_list[1][:len(salary_list[1])-1]) * exchange[salary_list[1][-1]]
        else:
            salary_list[0] = int(salary_list[0]) * exchange[salary_list[1][len(salary_list[1])-2:]]
            salary_list[1] = int(salary_list[1][:len(salary_list[1])-2]) * exchange[salary_list[1][len(salary_list[1])-2:]]
        d["salary"] = str(salary_list[0]) + '-' + str(salary_list[1]) 
    else:
        if salary_list[0][len(salary_list[0])-2:] != 'Br':
            salary_list[0] = int(salary_list[0][:len(salary_list[0])-1]) * exchange[salary_list[0][-1]]
        else:
            salary_list[0] = int(salary_list[0][:len(salary_list[0])-2]) * exchange[salary_list[0][len(salary_list[0])-2:]]
        d["salary"] = str(salary_list[0])

    # Приведение к корректному выводу experience
    list_experience = experience.split(':')[1].strip().split(' ')[0]
    if list_experience[0] in validate_digit and len(experience)>1:
        d["experience"] = list_experience[0] + '-' + list_experience[2]
    elif len(list_experience) == 1:
        d["experience"] = list_experience[0]
    else:
        d["experience"] = None

    # Приведение к корректному выводу company
    d["company"] = company

    # Приведение к корректному выводу description
    d["description"] = description

    # Приведение к корректному выводу skills
    d["skills"] = ', '.join(skills)

    # Приведение к корректному выводу created_at
    f = False
    created_at = created_at.replace('\xa0', ' ')
    created_at_str = ""
    for i in range(len(created_at)):
        if f:
            created_at_str += created_at[i]
        if created_at[i] == ' ' and created_at[i+1] in validate_digit:
            f = True
    for i in range(-1,-len(created_at_str)-1,-1):
        if created_at_str[i] == ' ' and created_at_str[i-1] in validate_digit:
            break

    d["created_at"] = created_at_str[:i]

    # Преобразование словаря в JSON и вывод результата
    result = json.dumps(d, ensure_ascii=False, indent=4)
    print(result)