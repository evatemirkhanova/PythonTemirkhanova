
# Сначала я создам класс "Stack" для представления стека.
# Класс будет иметь два метода:
#    "push" для добавления элемента в стек и "pop" для удаления и возврата верхнего элемента из стека.


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        # Создаем новый узел
        new_node = Node(data)

        # Присоединяем новый узел к началу списка
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None

        # Получаем значение верхнего элемента
        data = self.head.data

        # Перемещаем указатель на следующий узел
        self.head = self.head.next

        return data


# Cоздам класс "Node" для представления узла односвязного списка.
# Каждый узел будет содержать ссылку на следующий узел и данные.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Теперь, когда классы "Stack" и "Node" реализованы, я могу протестировать работу стека:

# Создаем новый экземпляр стека
stack = Stack()

# Добавляем элементы в стек
stack.push(1)
stack.push(2)
stack.push(3)

# Удаляем и выводим верхний элемент из стека
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.pop())  # None, так как стек пуст


# Этот код создаст стек на основе односвязного списка и продемонстрирует его работу, добавляя элементы и удаляя их из стека.
