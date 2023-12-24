import re
import csv

# Функция для чтения данных из CSV файла
def csv_reader(file_name:str) -> (list,list):
    reader = list()
    list_naming = list()
    with open(file_name, encoding='utf-8-sig') as file:
        count = 0
        for row in csv.reader(file, delimiter=','):
            if count == 0:
                list_naming = row
                count += 1
            else:
                reader.append(row)
    
    return reader, list_naming
# Функция для фильтрации данных из CSV файла
def csv_filer(reader, list_naming: list) -> list:
    data_vacancies = list()
	# Проходим через каждую строку данных в списке reader
    for data in reader:
        if '' not in data and len(data) == len(list_naming): # проверяем, что данные не содержат пустых значений и количество данных соответствует количеству столбцов
            d = dict() # создаем пустой словарь для хранения данных
            data[0] = data[0].replace('\xa0',' ') # заменяем некорректный символ в данных
            data[1] = re.sub(r'[ ]+',' ',re.sub(r'<.*?>', '', data[1]).strip()) # выполняем регулярное выражение для очистки данных и замены множественных пробелов
            data[1] = data[1].replace('  ',' ').replace('\xa0',' ') # заменяем некорректные символы в данных
            data[2] = ', '.join(data[2].split('\n')) # заменяем символы новой строки на запятую
            data[-1] = data[-1].replace('\xa0', ' ') # заменяем некорректные символы в данных
            data[4] = data[4].replace('FALSE', 'Нет').replace('TRUE', 'Да').replace('False', 'Нет').replace('True', 'Да') # заменяем значения в данных
            data[8] = data[8].replace('FALSE', 'Нет').replace('TRUE', 'Да').replace('False', 'Нет').replace('True', 'Да') # заменяем значения в данных
            for i in range(len(data)):
                d[list_naming[i]] = data[i]

            data_vacancies.append(d)

    return data_vacancies
# Функция для форматирования данных
def formatter(row: dict) -> dict:
	# Инициализируем словари соответствий для замены значений в данных
    d_money = {"AZN": "Манаты",
                "BYR": "Белорусские рубли",
                "EUR": "Евро",
                "GEL": "Грузинский лари",
                "KGS": "Киргизский сом",
                "KZT": "Тенге",
                "RUR": "Рубли",
                "UAH": "Гривны",
                "USD": "Доллары",
                "UZS": "Узбекский сум"}
    d_experience = {
        "noExperience": "Нет опыта",
        "between1And3": "От 1 года до 3 лет",
        "between3And6": "От 3 до 6 лет",
        "moreThan6": "Более 6 лет"}
	# Проходим через каждую пару ключ-значение в словаре данных
    for key,value in row.items():
        if value in d_money.keys():
            row[key] = d_money[value]
        if value in d_experience.keys():
            row[key] = d_experience[value]
        if key == "published_at":
            row[key] = '.'.join(list(reversed(value.split('T')[0].split('-'))))

    salary_from = ""
    c = 0
    a = row["salary_from"].split('.')[0]
    for  i in range(-1,-len(a)-1,-1): # Проходим через каждый символ оклада (от) в обратном порядке
        if c == 3:
            salary_from = ' ' + salary_from
            c = 0

        salary_from = a[i] + salary_from
        c+=1
         
    salary_to = ""
    c = 0
    a = row["salary_to"].split('.')[0]
    for  i in range(-1,-len(a)-1,-1): # Проходим через каждый символ оклада (до) в обратном порядке
        if c == 3:
            salary_to = ' ' + salary_to
            c = 0
        salary_to = a[i] + salary_to
        c+=1 
	# Создаем словарь с отформатированными данными о вакансии
    d = {"name":row["name"],"description":row["description"],"key_skills":row["key_skills"],"experience_id":row["experience_id"],"premium":row["premium"],"employer_name":row["employer_name"],"salary_gross": salary_from + ' - ' + salary_to
             + ' (' + row["salary_currency"] + ') ' + '(' + ("Без вычета налогов" if row["salary_gross"]=="Да" else "С вычетом налогов") + ')', "area_name":row["area_name"],"published_at":row["published_at"]} 

    return d
# Функция для печати отформатированных данных о вакансиях
def print_vacancies(data_vacancies: list, dic_naming: dict) -> None:
    for data in data_vacancies:
        d = formatter(data)
        for key,value in d.items():
            if key == "salary_gross":
                print("Оклад" + ': ' + str(value))
            elif key == "published_at":
                print("Дата публикации вакансии" + ': ' + str(value))
            else:
                print(dic_naming[key] + ': ' + str(value))

        if data_vacancies.index(data) != len(data_vacancies)-1:
            print('')
# Читаем данные из CSV файл
reader, list_naming = csv_reader(input())
# Фильтруем данные
data_vacancies = csv_filer(reader,list_naming)
# Задаем словарь заголовков столбцов
dic_naming = {"name":"Название",
			  "description":"Описание",
			  "key_skills":"Навыки",
			  "experience_id":"Опыт работы", 
			  "premium":"Премиум-вакансия",
			  "employer_name":"Компания", 
              "salary_from":"Нижняя граница вилки оклада",
			  "salary_to":"Верхняя граница вилки оклада", 
              "salary_gross":"Оклад указан до вычета налогов",
              "salary_currency":"Идентификатор валюты оклада",
			  "area_name":"Название региона", 
              "published_at":"Дата и время публикации вакансии"}
# Печатаем отформатированные данные о вакансиях
print_vacancies(data_vacancies, dic_naming)



