class Stack:
    def __init__(self):
        self.end = None

    def push(self, data):
        # Создаем новый узел
        new_node = Node(data)
        # Присоединяем новый узел к началу списка
        if self.end is None:
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end = new_node

    def pop(self):
        if self.end is None:
            raise IndexError("Stack is empty")
        # Получаем значение верхнего элемента
        data = self.end.data
        # Перемещаем указатель на следующий узел
        self.end = self.end.pref

        return data

    def print(self):
        if self.end is None:
            return None
        else:
            current = self.end
            while current:
                print(current.data)
                current = current.pref

class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.print()  # Вывод: 3, 2, 1

print(stack.pop())  # Вывод: 3

stack.print()  # Вывод: 2, 1

print(stack.pop()) # Вывод: 2
print(stack.pop()) # Вывод: 1
print(stack.pop()) # Вывод: IndexError: Stack is empty