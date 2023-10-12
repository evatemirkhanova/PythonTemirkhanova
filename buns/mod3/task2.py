s = int(input('Введите число: '))
print(*(bin(s)[2:],oct(s)[2:],hex(s)[2:] if s > 0 else 'Неверный ввод!'), sep = ', ')