from dataclasses import dataclass
from typing import Optional, List


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
class TwoLinkedListIterator:
    head: Node

    def clear(self) -> None:
        self.current = self.head

    def __post_init__(self) -> None:
        self.current: Node = self.head

    def __next__(self) -> Node:  # StopIteration
        if self.current is None:
            self.clear()
            raise StopIteration
        node = self.current
        self.current = self.current.get_next()
        return node

    def __iter__(self) -> 'TwoLinkedListIterator':
        return self


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

    def init(self, node: Node) -> None:
        self.set_head(node)
        self.set_tail(node)

    def is_empty(self) -> bool:
        return self.get_head() is None and self.get_tail() is None

    def is_head(self, node) -> bool:
        return self.get_head() == node

    def is_tail(self, node) -> bool:
        return self.get_tail() == node

    def add_to_head(self, node: Node) -> None:
        if self.is_empty():
            return self.init(node)

        old_head = self.get_head()
        node.set_next(old_head)
        node.set_prev(None)
        old_head.set_prev(node)
        self.set_head(node)

    def add_to_tail(self, node: Node) -> None:
        if self.is_empty():
            return self.init(node)

        old_tail = self.get_tail()
        old_tail.set_next(node)
        node.set_prev(old_tail)
        node.set_next(None)
        self.set_tail(node)

    def insert(self, after_node: Node, node: Node) -> None:
        if after_node in self:
            node.set_next(after_node.get_next())
            node.set_prev(after_node)
            after_next_node = after_node.get_next()
            if self.is_tail(after_node):
                self.set_tail(node)
            else:
                after_next_node.set_prev(node)

            after_node.set_next(node)

    def remove_from_head(self) -> Optional[Node]:
        if self.is_empty():
            return None

        head = self.get_head()
        if self.is_tail(head):
            self.clear()
            return head

        new_head = head.get_next()
        new_head.set_prev(None)
        self.set_head(new_head)
        return head

    def remove_from_tail(self) -> Optional[Node]:
        if self.is_empty():
            return None

        head = self.get_head()
        if self.is_tail(head):
            self.clear()
            return head

        tail = self.get_tail()
        new_tail = tail.get_prev()
        new_tail.set_next(None)
        self.set_tail(new_tail)
        return tail

    def remove(self, value: int, is_all: bool = False) -> None:
        for node in self:
            if node.value == value:
                if self.is_tail(node):
                    self.remove_from_tail()
                elif self.is_head(node):
                    self.remove_from_head()
                else:
                    node_prev = node.get_prev()
                    node_prev.set_next(node.get_next())
                    node.get_next().set_prev(node_prev)
                if not is_all:
                    break

    def reverse(self) -> None:
        current = self.get_head()
        self.set_tail(current)
        while current:
            current_next = current.get_next()
            current.set_next(current.get_prev())
            current.set_prev(current_next)
            if not current_next:
                self.set_head(current)
            current = current_next

    def find(self, value: int) -> Optional[Node]:
        for node in self:
            if node.get_value() == value:
                return node

    def find_all(self, value: int) -> List[Node]:
        return [node for node in self if node.get_value() == value]

    def clear(self) -> None:
        self.set_tail(None)
        self.set_head(None)

    def convert_to_array(self) -> List[Node]:
        return [node for node in self]

    def __iter__(self):
        return TwoLinkedListIterator(self.get_head())

    def __len__(self) -> int:
        return len(self.convert_to_array())


class AlternativeNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class AlternativeTwoLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head is None

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1

        node = self.head
        for _ in range(index):
            node = node.next

        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def getNode(self, index):
        head = self.head
        for _ in range(index):
            head = head.next
        return head

    def __addAtHead(self, node: Node) -> None:
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return

        new_node = AlternativeNode(val)
        if index == 0:
            self.__addAtHead(new_node)
        else:
            prev = self.getNode(index - 1)
            new_node.next = prev.next
            new_node.prev = prev
            if prev.next:
                prev.next.prev = new_node
            prev.next = new_node

        self.size += 1

    def __deleteAtHead(self) -> None:
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return

        if index == 0:
            self.__deleteAtHead()
        else:
            node = self.getNode(index - 1)
            node_next = node.next.next
            if node_next:
                node_next.prev = node
            node.next = node_next
        self.size -= 1
