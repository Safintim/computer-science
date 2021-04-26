from dataclasses import dataclass
from typing import Optional, List


@dataclass(eq=False)
class Node:
    value: int
    next: Optional['Node'] = None

    def set_value(self, value: int) -> None:
        self.value = value

    def get_value(self) -> int:
        return self.value

    def get_next(self) -> Optional['Node']:
        return self.next

    def set_next(self, node: Optional['Node']):
        self.next = node

    def __repr__(self):
        return 'Node({})'.format(self.get_value())


@dataclass
class LinkedListIterator:
    head: Node

    def clear(self) -> None:
        self.current = self.head

    def __post_init__(self) -> None:
        self.current: Node = self.head

    def __next__(self) -> Node:  # raises: StopIteration
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

    def set_head(self, node: Optional[Node]) -> None:
        self._head = node

    def set_tail(self, node: Optional[Node]) -> None:
        self._tail = node

    def is_empty(self):
        return self.get_head() is None and self.get_tail() is None

    def is_tail(self, node: Optional[Node]) -> bool:
        return self.get_tail() == node

    def is_head(self, node: Optional[Node]) -> bool:
        return self.get_head() == node

    def init(self, node: Node) -> None:
        self.set_head(node)
        self.set_tail(node)

    def add_to_head(self, node: Node) -> None:
        if self.is_empty():
            return self.init(node)

        node.set_next(self.get_head())
        self.set_head(node)

    def add_to_tail(self, node: Node) -> None:
        if self.is_empty():
            return self.init(node)

        tail = self.get_tail()
        tail.set_next(node)
        self.set_tail(node)

    def insert(self, after_node: Node, node: Node) -> None:
        if after_node in self:
            node.set_next(after_node.get_next())
            after_node.set_next(node)
            if self.is_tail(after_node):
                self.set_tail(node)

    def remove_from_head(self) -> Optional[Node]:
        if self.is_empty():
            return None

        head = self.get_head()
        if self.is_tail(head):
            self.clear()
        else:
            self.set_head(head.get_next())
        return head

    def remove_from_tail(self) -> Optional[Node]:
        if self.is_empty():
            return None

        head = self.get_head()
        if self.is_tail(head):
            self.clear()
            return head

        prev_tail = head
        for node in self:
            if self.is_tail(node.get_next()):
                prev_tail = node
                break

        tail = self.get_tail()
        prev_tail.set_next(None)
        self.set_tail(prev_tail)
        return tail

    def remove(self, value: int, is_all: bool = False) -> None:
        head = self.get_head()

        if self.is_empty():
            return None

        while head and head.get_value() == value:
            head = head.get_next()
            self.set_head(head)
            if not is_all:
                return

        if self.is_tail(head):
            return self.clear()

        current = head
        while current:
            current_next = current.get_next()
            if current_next and current_next.get_value() == value:
                current.set_next(current_next.get_next())
                if self.is_tail(current_next):
                    self.set_tail(current)
                if not is_all:
                    return
            else:
                current = current_next

    def reverse(self) -> None:
        head = self.get_head()
        tail = None
        self.set_tail(head)
        while head:
            new_head = head.get_next()
            if not new_head:
                self.set_head(head)
            head.set_next(tail)
            tail = head
            head = new_head

    def find(self, value: int) -> Optional[Node]:
        for node in self:
            if node.get_value() == value:
                return node

    def find_all(self, value: int) -> List[Node]:
        return [node for node in self if node.get_value() == value]

    def convert_to_array(self) -> List[Node]:
        return [node for node in self]

    def clear(self) -> None:
        self.set_tail(None)
        self.set_head(None)

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.get_head())

    def __len__(self) -> int:
        return len(self.convert_to_array())

    def has_cycle(self) -> bool:
        if self.is_empty():
            return False

        slow_runner = speed_runner = self.get_head()
        while speed_runner and speed_runner.get_next():
            slow_runner = slow_runner.get_next()
            speed_runner = speed_runner.get_next().get_next()
            if speed_runner == slow_runner:
                return True
        return False

    def detect_cycle(self) -> Optional[Node]:
        if self.is_empty():
            return None

        head = self.get_head()
        slow_runner = speed_runner = head
        while speed_runner and speed_runner.get_next():
            slow_runner = slow_runner.get_next()
            speed_runner = speed_runner.get_next().get_next()
            if speed_runner == slow_runner:
                while head != slow_runner:
                    head = head.get_next()
                    slow_runner = slow_runner.get_next()
                return head


def delete_from_tail(head: Node, n: int) -> Optional[Node]:
    if not head:
        return None
    slow = speed = head
    for _ in range(n):
        speed = speed.get_next()

    if not speed:
        return slow.get_next()

    while speed.get_next():
        slow = slow.get_next()
        speed = speed.get_next()
    slow.set_next(slow.get_next().get_next())
    return head


def intersection(head_a: Node, head_b: Node) -> Optional[Node]:
    point_a = head_a
    point_b = head_b
    while point_a != point_b:
        point_a = head_b if point_a is None else point_a.get_next()
        point_b = head_a if point_b is None else point_b.get_next()

    return point_a


def head(list_: LinkedList) -> Optional[Node]:
    return list_.get_head()


def tail(list_: LinkedList) -> LinkedList:
    new_list = LinkedList()
    new_head = list_.get_head().get_next()
    new_list.set_head(new_head)
    new_list.set_tail(list_.get_tail())
    return new_list


def odd_even_list(head: Node) -> Node:
    if not head:
        return head

    odd = head
    start_even = head.next
    even = start_even
    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = start_even
    return head


def palindrome(head: Node) -> bool:
    slow = fast = head

    while fast and fast.get_next():
        fast = fast.get_next().get_next()
        slow = slow.get_next()

    slow = reverse(slow)
    fast = head

    while slow:
        if slow.get_value() != fast.get_value():
            return False
        fast = fast.get_next()
        slow = slow.get_next()
    return True


def reverse(head: Node) -> Node:
    tail = None
    while head:
        new_head = head.get_next()
        head.set_next(tail)
        tail = head
        head = new_head
    return tail


class AlternativeNode:
    def __init__(self, v: int) -> None:
        self.val = v
        self.next = None


class AlternativeLinkedList:
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
        # node = AlternativeNode(val)
        # node.next = self.head.next
        # self.head = node
        # self.size += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        # node = AlternativeNode(val)
        # self.size += 1
        # if self.isEmpty():
        #     self.head = node
        # else:
        #     current = self.head
        #     while current.next:
        #         current = current.next
        #     current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return

        new_node = AlternativeNode(val)
        head = self.head
        if index == 0:
            new_node.next = head
            self.head = new_node
        else:
            for _ in range(index - 1):
                head = head.next

            new_node.next = head.next
            head.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return

        node = self.head
        if index == 0:
            self.head = node.next
        else:
            for _ in range(index - 1):
                node = node.next

            node.next = node.next.next
        self.size -= 1
