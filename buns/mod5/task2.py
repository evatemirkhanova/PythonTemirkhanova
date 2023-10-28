# необходимо создать класс Queue, представляющий собой очередь на основе структуры данных двусвязного списка.
# Для этого, в классе Queue нам потребуются методы добавления элемента в очередь (enqueue),
# удаления элемента из очереди (dequeue) и получения размера очереди (size).


# Создаем класс Node, который представляет узел двусвязного списка.
# Каждый узел содержит информацию (data),
# ссылку на следующий узел (next)
# и ссылку на предыдущий узел (prev).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Создаем класс Queue, который имеет атрибуты head и tail
# для хранения ссылок на первый и последний узлы очереди соответственно,
# а также атрибут size для хранения размера очереди.

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # метод добавления элемента в очередь
    def enqueue(self, data):                  
        new_node = Node(data)
        if self.head is None:                # Если очередь пустая
            self.head = new_node             # новый элемент становится и head, и tail.
            self.tail = new_node
        else:
            new_node.prev = self.tail        # Иначе, мы устанавливаем ссылку на новый элемент у текущего tail,
            self.tail.next = new_node        # а затем делаем новый элемент новым tail.
            self.tail = new_node
        self.size += 1
    
    # метод удаления 1-го элемента эл-та из очереди и возвращение его значения.
    def dequeue(self):
        if self.head is None:                # Если очередь пустая,
            raise IndexError("Queue is empty") # метод вызывает исключение
        
        data = self.head.data
        if self.head == self.tail:            # Если очередь содержит только один элемент,
            self.head = None                  # мы просто удаляем его и обнуляем значения head и tail.
            self.tail = None
        else:                                 # В противном случае,
            self.head = self.head.next         # перемещаем ссылку на следующий узел у head
            self.head.prev = None              # и удаляем ссылку на предыдущий узел.
        self.size -= 1
        return data

    # и метод получения размера очереди
    def size(self):
        return self.size

# Пример использования
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Выведет: 1
print(queue.dequeue())  # Выведет: 2
print(queue.size())     # Выведет: 1





