from dataclasses import dataclass
from typing import Optional


@dataclass(eq=False)
class Node:
    value: int
    next: Optional['Node'] = None

    def get_next(self) -> Optional['Node']:
        return self.next

    def set_next(self, node: Optional['Node']):
        self.next = node


@dataclass
class LinkedListIterator:
    head: Node

    def clear(self) -> None:
        self.current = self.head

    def __post_init__(self) -> None:
        self.current: Node = self.head

    def __next__(self) -> Node:  #raises: StopIteration
        if self.current is None:
            self.clear()
            raise StopIteration
        node = self.current
        self.current = self.current.get_next()
        return node

    def __iter__(self) -> 'LinkedListIterator':
        return self


@dataclass
class LinkedList:
    _head: Optional[Node] = None
    _tail: Optional[Node] = None

    def get_head(self) -> Optional[Node]:
        return self._head

    def get_tail(self) -> Optional[Node]:
        return self._tail

    def set_head(self, node: Node) -> None:
        self._head = node

    def set_tail(self, node: Node) -> None:
        self._tail = node

    def is_empty(self):
        return self.get_head() is None and self.get_tail() is None

    def is_tail(self, node: Node) -> bool:
        return self.get_tail() == node

    def add_to_head(self, node: Node) -> None:
        if self.is_empty():
            self.set_head(node)
            self.set_tail(node)
            return

        node.set_next(self.get_head())
        self.set_head(node)

    def add_to_tail(self, node: Node) -> None:
        if self.is_empty():
            self.set_head(node)
            self.set_tail(node)
            return
        tail = self.get_tail()
        tail.set_next(node)
        self.set_tail(node)

    def insert(self, after_node: Node, node: Node) -> None:
        if after_node in self:
            node.set_next(after_node.get_next())
            after_node.set_next(node)
            if self.is_tail(after_node):
                self.set_tail(node)

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.get_head())

