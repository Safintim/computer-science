from dataclasses import dataclass
from typing import Optional


@dataclass(eq=False)
class Node:
    value: int
    next: Optional['Node'] = None
    prev: Optional['Node'] = None

    def set_value(self, value: int) -> None:
        self.value = value

    def get_value(self) -> int:
        return self.value

    def get_next(self) -> Optional['Node']:
        return self.next

    def set_next(self, node: Optional['Node']):
        self.next = node

    def get_prev(self) -> Optional['Node']:
        return self.prev

    def set_prev(self, node: Optional['Node']):
        self.prev = node


@dataclass
class TwoLinkedList:
    _head: Optional['Node'] = None
    _tail: Optional['Node'] = None

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def set_head(self, node: Optional[Node]) -> None:
        self._head = node

    def set_tail(self, node: Optional[Node]) -> None:
        self._tail = node

    def is_empty(self) -> bool:
        return self.get_head() is None and self.get_tail() is None

    def init(self, node: Node) -> None:
        self.set_head(node)
        self.set_tail(node)

    def add_to_head(self, node: Node) -> None:
        if self.is_empty():
            return self.init(node)

        head = self.get_head()
        node.set_next(head)
        node.set_prev(None)
        head.set_prev(node)
        self.set_head(node)

    def add_to_tail(self, node: Node) -> None:
        if self.is_empty():
            return self.init(node)

        tail = self.get_tail()
        tail.set_next(node)
        node.set_prev(tail)
        node.set_next(None)