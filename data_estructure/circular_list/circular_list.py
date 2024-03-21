from data_estructure.circular_list.node_circular import Node
from typing import TypeVar, Generic

T = TypeVar('T')


class CircularList(Generic[T]):
    def __init__(self):
        self.__head: Node[T] | None = None
        self.__tail: Node[T] | None = None
        self.__size: int = 0
        self.__current: Node[T] | None = None
        self.__count: int = 0

    def __iter__(self):
        self.__current = self.__head

        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        data = self.__current.data
        if self.__current is self.__tail:
            self.__current = None
        else:
            self.__current = self.__current.next
        return data

    def get_size(self):
        return self.__size

    def is_empty(self) -> bool:
        return self.__head is None and self.__tail is None

    def find_at(self, index: int) -> Node[T]:
        current = self.__head
        for current_index in range(self.__size):
            if current is None:
                break
            elif current_index == index:
                return current
            else:
                current = current.next
        raise IndexError("La posicion no existe")

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            new_node.next = new_node
            new_node.previous = new_node
        else:
            self.__tail.next = new_node
            self.__head.previous = new_node
            new_node.previous = self.__tail
            self.__tail = new_node
            new_node.next = self.__head
        self.__size += 1

    def prepend(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.previous = new_node
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.previous = self.__tail
            new_node.next = self.__head
            self.__head.previous = new_node
            self.__tail.next = new_node
            self.__head = new_node

        self.__size += 1

    def insert_at(self, data: T, index):
        new_node = Node(data)
        if self.is_empty():
            raise IndexError("Lista vacia")
        elif index == 0:
            self.prepend(new_node)
        elif index == self.__size:
            self.append(new_node)
        else:
            aux_node = self.find_at(index)
            prev_node = aux_node.previous
            prev_node.next = new_node
            new_node.previous = prev_node
            new_node.next = aux_node
            aux_node.previous = new_node
            self.__size += 1

    def shift(self) -> T:
        if self.is_empty():
            raise OverflowError("Esta vacia")
        elif self.__tail is self.__head:
            current = self.__head
            self.__head.next = None
            self.__tail.next = None
            self.__size = 0

            return current.data
        else:
            current = self.__head
            self.__head = current.next
            self.__head.prev = self.__tail
            current.next = None
            current.previous = None
            self.__tail.next = self.__head
            self.__size -= 1
            return current.data

    def pop(self) -> T:
        if self.is_empty():
            raise MemoryError("Lista vacia")
        elif self.__tail is self.__head:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0

            return current.data
        else:
            current = self.__tail
            previous = current.previous
            self.__tail = previous
            self.__tail.next = self.__head
            current.next = None
            self.__size -= 1

            return current.data

    def delete_at(self, index):
        if self.is_empty() or index >= self.__size:
            raise IndexError("Index inválido")
        elif index == 0:
            data = self.shift()
            return data
        elif index == self.__size - 1:
            data = self.pop()
            return data
        elif self.__tail is self.__head:
            node = self.find_at(index)
            node.next = None
            node.previous = None
            self.__head = None
            self.__size = None
            self.__size = 0

            return node.data
        else:
            node = self.find_at(index)
            prev_node = node.previous
            next_node = node.next
            prev_node.next = next_node
            next_node.previous = prev_node
            node.previous = None
            node.next = None
            self.__size -= 1

            return node.data



