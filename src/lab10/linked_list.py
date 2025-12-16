from typing import Any, Optional, Iterator
class Node:
    def __init__(self, value: Any):
        self.value = value # Запоминаем данные
        self.next: Optional['Node'] = None # Указатель на следующий узел

class SinglyLinkedList:
    def __init__(self, iterable=None):
        self.head: Optional[Node] = None # Указатель на начало (голову) 
        self.tail: Optional[Node] = None # Указатель на конец (хвост)
        self._size: int = 0
        if iterable:
            for item in iterable:
                self.append(item)
                
    def append(self, value): # добавление элемента в конец списка
        new_node = Node(value)
        
        if self.head is None: # Проверка на пустой список
            self.head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1
        
    def prepend(self, value: Any) -> None: # Добавление элемента в начало списка
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        if self._size == 0:
            self.tail = new_node
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("Индекс выходит за пределы допустимого диапазона")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return
        
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    def remove(self, value: Any) -> None: # Удаление первого вхождения значения value.
        if not self.head:
            raise ValueError(f"{value} not in list")

        # Случай 1 : удаление головы
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            if self._size == 0:
                self.tail = None
            return
        # Случай 2 : Удаление из середины или конца
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                if current.next is None: # обновление tail, если удален последний элемент
                    self.tail = current
                self._size -= 1
                return
            current = current.next
        raise ValueError(f"{value} not in list")
    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size
    
    def __repr__(self) -> str: # Красивый вывод: [A] -> [B] -> [C] -> None
        parts = []
        current = self.head
        while current:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)
    
if __name__ == "__main__":
    print("Демонстрация  SINGLY LINKED LIST")
    sll = SinglyLinkedList()
    sll.append(16)
    sll.append(1)
    print(f"Создан список : {sll}")
    sll.prepend(33)
    print(f"В начало добавлено число : {sll}")
    sll.insert(1,6)
    print(f"После первого индекса добавлено число: {sll}")
    sll.remove(1) 
    print(f"Удален tail(хвост): {sll}")
    print(f"Новый Tail: {sll.tail.value if sll.tail else 'None'}")
    for i in sll:
        print(f"Элемент: {i}")