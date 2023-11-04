"""
#1. Создаем класс DoubleElement:
class DoubleElement:
    #Здесь мы определяем конструктор класса, который принимает произвольное количество аргументов и сохраняет их в переменную lst.
    def __init__(self, *lst):
        pass

    def __iter__(self): # Метод __iter__ возвращает сам объект класса и позволяет использовать его в цикле for.
        pass

    def __next__(self): # Метод __next__ будет вызываться при каждой итерации цикла for.
        pass
        raise StopIteration # В данном случае мы просто вызываем исключение StopIteration, чтобы остановить итерацию.

Теперь, когда у нас есть базовая структура класса, можем приступить к реализации его функциональности.
"""

class DoubleElement:
    def __init__(self, *lst):
        self.lst = list(lst)
        self.index = 0

    # Метод __iter__ должен вернуть сам объект класса:
    def __iter__(self):
        return self
    
    # В методе __next__ нужно реализовать логику итерации по списку и возвращения пары элементов:
    def __next__(self):
        
        if len(self.lst) > 0:                        # проверяем, если список lst не пустой
            first_element = self.lst.pop(0)          # то извлекаем из него первый элемент и сохраняем его в переменную first_element. 
            if len(self.lst) > 0:                    # Далее, если список еще не пустой,
                second_element = self.lst.pop(0)     # извлекаем из него следующий элемент и сохраняем его в переменную second_element,
            else:
                second_element = None                #  иначе присваиваем None переменной second_element.
            return (first_element, second_element)   # Затем, возвращаем пару элементов (first_element, second_element)
        
        else:                                        # Если список lst становится пустым
            raise StopIteration                      # вызываем исключение StopIteration.

"""
Теперь, когда класс DoubleElement полностью реализован,
мы можем создать экземпляры этого класса и использовать их в цикле for для вывода ожидаемых результатов.
"""

# Создаем экземпляр класса DoubleElement с разными списками:

dL = DoubleElement(1,2,3,4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1,2,3,4,5)
for pair in dL:
    print(pair)

"""
В результате выполнения кода мы получим ожидаемый вывод:

(1, 2)
(3, 4)

(1, 2)
(3, 4)
(5, None)


Таким образом, мы реализовали класс DoubleElement, который при итерации возвращает пару элементов из переданного ему списка.
"""