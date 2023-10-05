s = input('Введите 3 числа: ')

whitespace1 = s.find(' ')
first_number = int(s[:whitespace1])

whitespace2 = s.find(' ', whitespace1+1)
second_number = int(s[whitespace1+1:whitespace2])

whitespace3 = s.find(' ', whitespace2+1)
third_number = int(s[whitespace2+1:])

if (-1000 <= first_number <= 1000) and (-1000 <= second_number <= 1000) and (-1000 <= third_number <= 1000):
    total= first_number + second_number + third_number
    total -= max(first_number, second_number, third_number) + min(first_number, second_number, third_number)
    print(total)
else:
    print("Число вне допустимого диапазона")