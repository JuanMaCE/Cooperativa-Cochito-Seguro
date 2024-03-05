from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T, next_node=None, prev_node=None):
        self.__data = data
        self.__next: Node | None = next_node
        self.__prev: Node | None = prev_node

    def __str__(self):
        return str(self.__data)

    def __int__(self):
        return int(self.__data)

    @property
    def next(self):
        return self.__next

    @property
    def data(self):
        return self.__data

    @next.setter
    def next(self, new_next: Node[T]):
        self.__next = new_next
