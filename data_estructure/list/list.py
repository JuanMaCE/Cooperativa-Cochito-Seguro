from data_estructure.list.node_list import Node
from typing import TypeVar, Generic

T = TypeVar("T")


class List(Generic[T]):
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
        if index == 0:
            self.prepend(data)
        elif index == len(self) - 1:
            self.append(data)
        elif index < 0 or index > len(self)-1:
            raise IndexError("La pocicion es invalida")
        else:
            new_node = Node(data)
            previous_node = self.find_at(index-1)
            new_node.next = previous_node.next
            new_node.prev = previous_node
            previous_node.next = new_node
            self.__size += 1

    def insertar_ordenado(self, data):
        index = 0
        if self.is_empty():
            self.append(data)
        else:
            min = None
            for number in self:
                if min == None:
                    min = int(data)
                elif int(data) < int(min):
                    min = int(data)
            for number in self:
                if int(number) <= int(data):
                    self.insert_at(data, index)
                    break
                elif int(data) < int(min):
                    self.append(data)
                    break
                index += 1

    def shift(self):
        if self.is_empty():
            raise ReferenceError("no hay datos en la lista")
        elif len(self) == 1:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data
        else:
            current = self.__head
            self.__head = current.next
            current.next = None
            self.__size -= 1

            return current.data

    def pop(self):
        if self.is_empty():
            raise ReferenceError("no hay datos en la lista")
        elif self.__head is self.__tail:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return current.data
        else:
            current = self.__tail
            previous = self.find_at(len(self)-2)
            self.__tail = previous
            previous.next = None
            self.__size -= 1

            return current.data

    def remove_at(self, index: int):
        if index < 0 or index >= len(self):
            raise IndexError("La pocicion no existe")
        elif index == 0:
            return self.shift()
        elif index == len(self)-1:
            return self.pop()
        else:
            current_node = self.find_at(index)
            previous_node = self.find_at(index-1)
            next_node = current_node.next
            previous_node.next = next_node
            current_node.next = None
            self.__size -= 1

            return current_node.data

    def find_at(self, index: int):
        current_index = 0
        current = self.__head

        while current is not None:
            if current_index == index:
                return current
            else:
                current = current.next
                current_index += 1

        raise IndexError("La pocicion no existe")

    def imprimir_inverso(self):
        lista_al_reves = ""
        tamanio = self.__size - 1
        while True:
            lista_al_reves += " - " + str(self.find_at(tamanio))
            tamanio -= 1
            if tamanio == 0:
                lista_al_reves += " - " + str(self.find_at(tamanio))
                break
        return lista_al_reves

    def invertir_lista(self):
        current = self.__tail
        while True:
            current.next = current.prev
            current = current.next
            if current == self.__head:
                current2 = self.__head
                self.__head = self.__tail
                self.__tail = current2
                self.__tail.next = None
                break

        current = self.__head
        while True:
            if current == self.__head:
                current.prev = None
                current = current.next
                current.prev = self.__head
            else:
                previous = current
                current = current.next
                current.prev = previous
                if current == self.__tail:
                    break

    def intercambiar_extremos(self):
        nodo1 = Node(self.__head.data)
        nodo2 = Node(self.__tail.data)
        self.pop()
        self.shift()
        self.prepend(nodo2)
        self.append(nodo1)

    def concatenar(self, lista):
        for dato in lista:
            self.append(dato)

    def ordenar(self):
        lista = " "
        aux = List[int]()
        for number in self:
            aux.insertar_ordenado(number)
        for i in aux:
            lista += str(i) + " - "
        return lista

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        data = self.__current.data
        self.__current = self.__current.next

        return data

    def __len__(self):
        cont = 0
        for _ in self:
            cont += 1
        return cont
