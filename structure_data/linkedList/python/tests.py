from typing import Union, List

import pytest

from linked_list import Node, LinkedList, head, tail


def create_nodes(
    count: int,
    start_value: int = 100
) -> Union[List[Node], Node]:
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


def test_linked_list_init():
    list_ = LinkedList()
    node = create_nodes(count=1)
    list_.init(node)
    assert list_.get_head() == node
    assert list_.get_tail() == node


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


def test_linked_list_get_array():
    list_ = LinkedList()
    nodes = create_nodes(6)
    for node in nodes:
        list_.add_to_head(node)
    array = list_.convert_to_array()
    assert nodes[::-1] == array


def test_linked_list_len():
    len_list = 6
    list_ = create_linked_list(node_count=len_list)
    assert len(list_) == len_list


def test_linked_list_clear():
    list_ = create_linked_list(node_count=6)
    list_.clear()
    assert list_.is_empty()


def test_linked_list_remove_from_head_empty():
    list_ = LinkedList()
    node = list_.remove_from_head()
    assert node is None


def test_linked_list_remove_from_head_one_node():
    list_ = LinkedList()
    list_.add_to_head(create_nodes(1))
    list_.remove_from_head()
    assert list_.is_empty()


def test_linked_list_remove_from_head_two_node():
    list_ = create_linked_list()
    tail = list_.get_tail()
    list_.remove_from_head()
    assert list_.get_head() == tail
    assert list_.get_tail() == tail


def test_linked_list_remove_from_head():
    list_ = create_linked_list(node_count=6)
    head = list_.get_head()
    head_next = head.get_next()
    list_.remove_from_head()
    assert list_.get_head() == head_next


def test_linked_list_remove_from_tail_empty():
    list_ = LinkedList()
    node = list_.remove_from_tail()
    assert node is None


def test_linked_list_remove_from_tail_one_node():
    list_ = LinkedList()
    list_.add_to_head(create_nodes(1))
    list_.remove_from_tail()
    assert list_.is_empty()


def test_linked_list_remove_from_tail():
    list_ = create_linked_list(node_count=6)
    old_array = list_.convert_to_array()
    old_tail = list_.get_tail()
    node = list_.remove_from_tail()
    new_array = list_.convert_to_array()
    assert len(list_) == 5
    assert old_tail == node
    assert old_array[:-1] == new_array


def test_linked_list_find():
    list_ = create_linked_list(node_count=6)
    assert bool(list_.find(value=100))
    assert list_.find(value=200) is None


def test_linked_list_find_all():
    nodes = [Node(100), Node(200), Node(100), Node(300), Node(100)]
    list_ = LinkedList()
    for node in nodes:
        list_.add_to_head(node)

    expected = [node for node in nodes[::-1] if node.get_value() == 100]
    assert list_.find_all(value=100) == expected


def test_linked_list_remove_by_value():
    nodes = [Node(100), Node(200), Node(100), Node(300), Node(100)]
    list_nodes = nodes[::-1]
    list_ = LinkedList()
    for node in nodes:
        list_.add_to_head(node)

    list_.remove(value=100)
    del list_nodes[0]
    assert list_.convert_to_array() == list_nodes

    list_.remove(value=200)
    del list_nodes[2]
    assert list_.convert_to_array() == list_nodes


def test_linked_list_remove_by_value_all():
    nodes = [Node(100), Node(200), Node(100), Node(300), Node(100)]
    list_nodes = nodes[::-1]
    list_ = LinkedList()
    for node in nodes:
        list_.add_to_head(node)

    list_.remove(value=100, is_all=True)
    expected = [node for node in list_nodes if node.get_value() != 100]
    assert list_.convert_to_array() == expected
    assert len(list_) == 2


def test_linked_list_reverse():
    list_ = create_linked_list(node_count=6)
    old_array = list_.convert_to_array()
    expected = old_array[::-1]
    list_.reverse()
    assert list_.convert_to_array() == expected
    assert list_.get_tail() == expected[-1]
    assert list_.get_head() == expected[0]


def test_head():
    list_ = create_linked_list(node_count=6)
    assert head(list_) == list_.get_head()


def test_tail():
    list_ = create_linked_list(node_count=6)
    old_head = list_.get_head()
    old_list = list_.convert_to_array()
    list_ = tail(list_)
    expected = list_.convert_to_array()
    assert list_.get_head() == old_head.get_next()
    assert old_list[1:] == expected
