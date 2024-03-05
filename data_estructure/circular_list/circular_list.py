from node_circular import Node
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
        data = self.__current
        if self.__current is self.__tail.next and self.__count == 1:
            self.__count = 0
            raise StopIteration
        self.__current = self.__current.next
        self.__count = 1
        return data

    def imprimit_hacia_atras(self):
        lista_al_reves = " "
        tamanio = self.__size - 1
        while True:
            lista_al_reves += " - " + str(self.find_at(tamanio))
            tamanio -= 1
            if tamanio == 0:
                lista_al_reves += " - " + str(self.find_at(tamanio))
                break
        return lista_al_reves

    def inversrion_list(self):
        new_head = self.__tail
        new_tail = self.__head
        self.__tail.next = None
        tamanio = self.__size - 1
        current = new_head
        current.next = self.find_at(tamanio)
        new_list = (CircularList[str]())
        while True:
            current.next = self.find_at(tamanio)
            new_list.append(current.next)
            tamanio -= 1
            if tamanio == 0:
                break
        self.__head = new_head
        self.__current = self.__head.next
        for i in new_list:
            self.__current = i
            self.__current = self.__current.next

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__tail.next = self.__head
        self.__size += 1

    def prepend(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
            self.__tail.next = self.__head
        self.__size += 1

    def is_empty(self) -> bool:
        return self.__head is None and self.__tail is None

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
            current.next = None
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
            previous = self.find_at(self.__size - 2)
            self.__tail = previous
            self.__tail.next = self.__head
            current.next = None
            self.__size -= 1

            return current.data

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

    def find_index(self, data: T):
        contador = 0
        for value in self:
            if value == data:
                print(" se encontro en: ", contador)
                return contador
            contador += 1

    def insert_at(self, data: int, index: int):
        if index == 0:
            self.prepend(data)
        if index == self.__size:
            self.append(data)
        elif 0 < index <= self.__size:
            new_node = Node(data)
            previus = self.find_at(index - 1)
            new_node.next = previus.next
            previus.next = new_node
            self.__size += 1
        else:
            raise Exception(" la posición no existe")

