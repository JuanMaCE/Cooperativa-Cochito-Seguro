from node import Node
from typing import TypeVar, Generic


T = TypeVar("T")


class ListD(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size = 0
        self.__current: Node[T] | None = None

    def is_empty(self):
        return self.__head is None and self.__tail is None

    def prepend(self, data: T):
        new_node = Node(data, self.__head)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            self.__head.prev = new_node
            self.__head = new_node
            self.__size += 1

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
            self.__size += 1

    def insert_at(self, data: T, index: int):
        new_node = Node(data)
        condicion = 0 < index > self.__size
        if index == 0:
            self.prepend(new_node)
        elif index == self.__size:
            self.append(new_node)
        elif condicion:
            IndexError(" No existe el index que mando ")
        else:
            previuos = self.find_at(index - 1)
            new_node.next = previuos.next
            previuos.next = None
            previuos.next = new_node

    def find_at(self, index):
        condicion = 0 < index > self.__size
        if self.is_empty():
            Exception("No se encontro el valor")
        elif condicion:
            IndexError(" No existe el index que mando ")
        else:
            current_index = 0

            current = self.__head
            while current is not None:
                if index == current_index:
                    return current
                else:
                    current_index += 1
                    current = current.next
            raise IndexError("La posición no existe: ")

    def find_by(self, data):
        if self.is_empty():
            Exception("No se encontro el valor")
        else:
            current_index = 0
            current = self.__head
            while current is not None:
                if data == current.data:
                    return current_index
                else:
                    current_index += 1
                    current = current.next
            raise IndexError("La posición no existe: ")

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        data = self.__current.data
        self.__current = self.__current.next
        return data

    def shift(self):
        if self.is_empty():
            raise IndexError(" la lista esta vacia")
        else:
            current = self.__head
            new_head = self.__head.next
            new_head.prev = None
            self.__head = new_head
            return current

    def pop(self):
        if self.is_empty():
            raise IndexError("la lista esta vacia")
        else:
            current = self.__tail
            new_tail = self.__tail.prev
            new_tail.next = None
            self.__tail = new_tail
            return current

    def eliminate_at(self, index: int):
        if self.is_empty():
            raise IndexError("la lista esta vacia")
        if index == 0:
            self.shift()
        elif index == self.__size - 1:
            self.pop()
        else:
            current = self.find_at(index)
            previous = current.prev
            previous.next = current.next
            current.next = None
            current.prev = None
            return current
