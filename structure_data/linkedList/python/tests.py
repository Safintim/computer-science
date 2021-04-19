from __future__ import annotations
from typing import Union

import pytest

from linked_list import Node, LinkedList


def create_nodes(count: int, start_value: int=100) -> Union[list[Node], Node]:
    if count == 1:
        return Node(start_value)
    return [Node(start_value + i) for i in range(count)]


def create_linked_list(node_count=2) -> LinkedList:
    list_ = LinkedList()
    for node in create_nodes(node_count):
        list_.add_to_head(node)
    return list_


def test_node_create():
    node1 = Node(value=100, next=None)
    node2 = Node(value=200, next=node1)
    node3 = Node(value=300, next=node2)
    assert node1.value == 100
    assert node1.next is None
    assert node2.next == node1
    assert node3.next == node2


def test_node_set_next():
    node1 = Node(value=100, next=None)
    node2 = Node(value=200, next=None)
    node1.set_next(node2)
    assert node1.next == node2


def test_linked_list_create():
    list_ = LinkedList()
    assert list_.get_head() is None
    assert list_.get_tail() is None


def test_linked_list_add_to_head():
    list_ = LinkedList()
    node1, node2, node3 = create_nodes(count=3)
    
    list_.add_to_head(node1)
    assert list_.get_head() == node1
    assert list_.get_tail() == node1
    
    list_.add_to_head(node2)
    assert list_.get_head() == node2
    assert node2.next == node1
    assert list_.get_tail() == node1

    list_.add_to_head(node3)
    assert list_.get_head() == node3
    assert node3.next == node2
    assert list_.get_tail() == node1


def test_linked_list_add_to_tail():
    list_ = LinkedList()
    node1, node2, node3 = create_nodes(count=3)
    
    list_.add_to_tail(node1)
    assert list_.get_head() == node1
    assert list_.get_tail() == node1
    
    list_.add_to_tail(node2)
    assert list_.get_head() == node1
    assert node1.next == node2
    assert list_.get_tail() == node2

    list_.add_to_tail(node3)
    assert list_.get_head() == node1
    assert node2.next == node3
    assert list_.get_tail() == node3


def test_linked_list_iterator():
    list_ = LinkedList()
    list_.add_to_head(create_nodes(count=1))

    iterator = iter(list_)
    with pytest.raises(StopIteration):
        next(iterator)
        next(iterator)


def test_linked_list_contains():
    list_ = create_linked_list()
    node = create_nodes(count=1)

    assert list_.get_head() in list_
    assert node not in list_


def test_linked_list_insert_to_empty():
    list_ = LinkedList()
    node1, node2 = create_nodes(count=2)
    list_.insert(node1, node2)
    assert list_.is_empty()


def test_linked_list_insert_to_one_node():
    list_ = LinkedList()
    node1, node2 = create_nodes(count=2)
    list_.add_to_head(node1)
    
    list_.insert(node1, node2)
    assert node1.get_next() == node2
    assert list_.get_head() == node1
    assert list_.get_tail() == node2


def test_linked_list_insert_to_head():
    list_ = create_linked_list(node_count=6)
    node = create_nodes(count=1)
    head, afterHead = list_.get_head(), list_.get_head().get_next()
    
    list_.insert(head, node)
    assert list_.get_head() == head
    assert head.get_next() == node
    assert node.get_next() == afterHead
    
    
def test_linked_list_insert_to_tail():
    list_ = create_linked_list(node_count=6)
    node = create_nodes(count=1)
    tail = list_.get_tail()
    list_.insert(tail, node)
    assert list_.get_tail() == node
    assert tail.get_next() == node


def test_linked_list_insert():
    list_ = create_linked_list(node_count=6)
    prev_node = list_.get_head().get_next()
    next_node = prev_node.get_next()
    node = create_nodes(count=1)
    list_.insert(prev_node, node)
    assert prev_node.get_next() == node
    assert node.get_next() == next_node
