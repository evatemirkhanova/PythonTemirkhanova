# Импортировать модуль re (регулярные выражения) и модуль requests.
import re
import requests

# Получить содержимое веб-страницы:
url = 'http://www.columbia.edu/~fdc/sample.html' # Сохранить URL веб-страницы в переменную url.
response = requests.get(url)                     # Получить содержимое веб-страницы по указанному URL и сохранить ответ в переменной response.
content = response.text                          # Извлечь текст из полученного ответа и сохранить его в переменной content

# Извлекать подзаголовки с помощью регулярных выражений в содержимом веб-страницы и сохранить их в список subheadings.
subheadings = re.findall(r'<h3 id=".*?">(.*?)</h3>', content)

# Вывести список подзаголовков на экран
print(subheadings)
