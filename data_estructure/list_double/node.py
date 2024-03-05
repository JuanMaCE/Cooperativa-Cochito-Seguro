from __future__ import annotations
from typing import TypeVar, Generic


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T, next_node=None, previus_node=None):
        self.__data = data
        self.__next: Node | None = next_node
        self.__prev: Node | None = previus_node

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    @property
    def data(self):
        return self.__data

    def __str__(self):
        return str(self.__data)

    def __int__(self):
        return int(self.__data)

    @next.setter
    def next(self, new_next: Node[T]):
        self.__next = new_next

    @prev.setter
    def prev(self, value):
        self.__prev = value
