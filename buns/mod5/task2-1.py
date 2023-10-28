# Создаем класс Node, который представляет узел двусвязного списка.
# Каждый узел содержит информацию (data),
# ссылку на следующий узел (next)
# и ссылку на предыдущий узел (prev).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Создаем класс Queue, который имеет атрибуты start и end
# для хранения ссылок на первый и последний узлы очереди соответственно
class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        
    def pop(self): # возвращаем элемент val из начала списка с удалением из списка
        if self.start is None:
            raise IndexError("Queue is empty")

        val = self.start.data
        
        if self.start.next is not None:
            self.start.next.prev = None # чел вышел из очереди
            
        self.start = self.start.next # теперь 1-ый эл-т очереди сменился
        
        if self.start is None: # если дальше эл-тов не последовало
            self.end = None    # тогда, что конец, что начало - None

        return val # возвращаем удаленный элемент

    # добавление элемента val в конец списка
    def push(self, val):
        new_node = Node(val)
        if self.start is None:                # Если очередь пустая
            self.start = new_node             # новый элемент становится и start, и end.
            self.end = new_node
        else:
            new_node.prev = self.end        # Иначе, мы устанавливаем ссылку на новый элемент у текущего end,
            self.end.next = new_node        # а затем делаем новый элемент новым end.
            self.end = new_node

    # вставить элемент val между элементами с номерами n-1 и n
    def insert(self, n, val):
        if n <= 0:
            self.push(val)
            return

        new_node = Node(val)
        current = self.start
        count = 1
        while current is not None and count < n:
            current = current.next
            count += 1

        if current is None:
            new_node.prev = self.end
            self.end.next = new_node
            self.end = new_node
        else:
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

    def print(self):
        current = self.start
        result = []
        while current is not None:
            result.append(current.data)
            current = current.next
        print(result)


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)

#Выведет список состоящий из 1,2 и 3
queue.print() 
#Добавит 5ку по индексу n-1 (2-1=1)
queue.insert(2, 5)
#Добавит 4ку по индексу n-1 (4-1=3)
queue.insert(4, 4)

queue.print()

print(queue.pop()) #удалит 0й элемент из списка - останется 4 числа
print(queue.pop()) #удалит 0й элемент из списка - останется 3 числа

queue.print()