from collections import deque

class Stack:
    def __init__(self):
        self._data: list[any] = []
        
    def push(self, item: any) -> None:
        self._data.append(item)
    
    def pop(self) -> any:
        if self.is_empty():
            raise IndexError("pop from 'пустой' stack")
        return self._data.pop()
    
    def peek(self):
        if not self._data:
            return None
        return self._data[-1] # первый элемент без удаления
    
    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __repr__(self):
        return f"Stack({self._data})" # Превращаем список в строку вида "Stack([1, 2, 3])"
    
class Queue:
    def __init__(self):
        self._data: deque[any] = deque()

    def enqueue(self, item: any) -> None:
        self._data.append(item) #добавление элемента в конец очереди

    def dequeue(self) -> any:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft() #взять элемент из начала очереди

    def peek(self):
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)
    
    def __repr__(self):
        return f"Queue({list(self._data)})" # Превращаем dequeue в обычный список для красивого вывода

if __name__ == "__main__":
    print("Демонстрация STACK")
    stack = Stack()
    stack.push(16)
    stack.push(1)
    stack.push(33)
    print(f"Stack после добавления чисел : {stack}")
    print(f"Верхнее число: {stack.peek()}")
    print(f"Извлечение числа : {stack.pop()}")
    print(f"Стек после извлечения: {stack}")
    print(f'Стек : {stack._data}')
    print(f"Длина стека : {len(stack)}")
    print("                                ")
    print("Демонстрация QUEUE")
    queue = Queue()
    queue.enqueue("Первый")
    queue.enqueue("Третий")
    queue.enqueue(4)
    queue.enqueue(5)
    print(f"Очередь после добавления : {queue}")
    first = queue.peek()
    print(f"Первый в очереди: {first}")
    dequeued = queue.dequeue()
    print(f"Функция dequeue: {dequeued}")
    print(f"Очередь после dequeue: {queue}")