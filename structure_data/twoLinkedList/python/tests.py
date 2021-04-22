from typing import Union, List

import pytest

from two_linked_list import Node, TwoLinkedList


def create_nodes(
    count: int,
    start_value: int = 100
) -> Union[List[Node], Node]:
    if count == 1:
        return Node(start_value)
    return [Node(start_value + i) for i in range(count)]


def create_two_linked_list(node_count=2) -> TwoLinkedList:
    list_ = TwoLinkedList()
    for node in create_nodes(node_count):
        list_.add_to_head(node)
    return list_


def test_create_node():
    node1 = Node(100)

    assert node1.get_value() == 100
    assert node1.get_next() is None
    assert node1.get_prev() is None

    node2 = Node(100)
    node3 = Node(200)
    node4 = Node(300)
    node2.set_next(node3)
    node2.set_prev(node4)

    assert node2.get_next() == node3
    assert node2.get_prev() == node4


def test_create_two_linked_list():
    list_ = TwoLinkedList()

    assert list_.get_head() is None
    assert list_.get_tail() is None


def test_two_linked_list_init():
    list_ = TwoLinkedList()
    node = create_nodes(count=1)
    list_.init(node)
    assert list_.get_head() == node
    assert list_.get_tail() == node


def test_two_linked_list_add_to_head_empty():
    list_ = TwoLinkedList()
    node = create_nodes(1)
    list_.add_to_head(node)
    assert list_.get_head() == node
    assert list_.get_tail() == node


def test_two_linked_list_add_to_head():
    list_ = TwoLinkedList()
    node1 = create_nodes(1)
    list_.init(node1)

    node2 = create_nodes(1)
    list_.add_to_head(node2)
    assert list_.get_head() == node2
    assert list_.get_tail() == node1
    assert list_.get_tail().get_prev() == node2


def test_two_linked_list_add_to_tail_empty():
    list_ = TwoLinkedList()
    node = create_nodes(1)
    list_.add_to_tail(node)
    assert list_.get_head() == node
    assert list_.get_tail() == node


def test_two_linked_list_add_to_tail():
    list_ = TwoLinkedList()
    node1 = create_nodes(1)
    list_.init(node1)

    node2 = create_nodes(1)
    list_.add_to_tail(node2)
    assert list_.get_tail() == node2
    assert list_.get_tail().get_prev() == node1


def test_linked_list_iterator():
    list_ = TwoLinkedList()
    list_.add_to_head(create_nodes(count=1))

    iterator = iter(list_)
    with pytest.raises(StopIteration):
        next(iterator)
        next(iterator)


def test_two_linked_list_contains():
    list_ = create_two_linked_list()
    node = create_nodes(count=1)

    assert list_.get_head() in list_
    assert node not in list_


def test_two_linked_list_insert_to_empty():
    list_ = TwoLinkedList()
    node1, node2 = create_nodes(count=2)
    list_.insert(node1, node2)
    assert list_.is_empty()


def test_two_linked_list_insert_to_one_node():
    list_ = TwoLinkedList()
    node1, node2 = create_nodes(count=2)
    list_.add_to_head(node1)

    list_.insert(node1, node2)
    assert node1.get_next() == node2
    assert node2.get_prev() == node1
    assert list_.get_head() == node1
    assert list_.get_tail() == node2


def test_two_linked_list_insert_to_head():
    list_ = create_two_linked_list(node_count=6)
    node = create_nodes(count=1)
    head, after_head = list_.get_head(), list_.get_head().get_next()

    list_.insert(head, node)
    assert list_.get_head() == head
    assert head.get_next() == node
    assert node.get_next() == after_head
    assert node.get_prev() == head
    assert after_head.get_prev() == node


def test_two_linked_list_insert_to_tail():
    list_ = create_two_linked_list(node_count=6)
    node = create_nodes(count=1)
    old_tail = list_.get_tail()
    list_.insert(old_tail, node)
    assert list_.get_tail() == node
    assert old_tail.get_next() == node
    assert node.get_prev() == old_tail


def test_two_linked_list_insert():
    list_ = create_two_linked_list(node_count=6)
    prev_node = list_.get_head().get_next()
    next_node = prev_node.get_next()
    node = create_nodes(count=1)
    list_.insert(prev_node, node)
    assert prev_node.get_next() == node
    assert node.get_prev() == prev_node
    assert node.get_next() == next_node
    assert next_node.get_prev() == node


def test_two_linked_list_convert_to_array():
    list_ = TwoLinkedList()
    nodes = create_nodes(6)
    for node in nodes:
        list_.add_to_head(node)
    array = list_.convert_to_array()
    assert nodes[::-1] == array


def test_two_linked_list_len():
    len_list = 6
    list_ = create_two_linked_list(node_count=len_list)
    assert len(list_) == len_list


def test_two_linked_list_clear():
    list_ = create_two_linked_list(node_count=6)
    list_.clear()
    assert list_.is_empty()


def test_two_linked_list_remove_from_head_empty():
    list_ = TwoLinkedList()
    node = list_.remove_from_head()
    assert node is None


def test_two_linked_list_remove_from_head_one_node():
    list_ = TwoLinkedList()
    head = create_nodes(1)
    list_.add_to_head(head)
    node = list_.remove_from_head()
    assert list_.is_empty()
    assert node == head


def test_two_linked_list_remove_from_head_two_node():
    list_ = create_two_linked_list()
    tail = list_.get_tail()
    list_.remove_from_head()
    assert list_.get_head() == tail
    assert list_.get_tail() == tail
    assert list_.get_tail().get_prev() is None


def test_two_linked_list_remove_from_head():
    list_ = create_two_linked_list(node_count=6)
    head = list_.get_head()
    head_next = head.get_next()
    list_.remove_from_head()
    assert list_.get_head() == head_next
    assert head_next.get_prev() is None


def test_two_linked_list_remove_from_tail_empty():
    list_ = TwoLinkedList()
    node = list_.remove_from_tail()
    assert node is None


def test_two_linked_list_remove_from_tail_one_node():
    list_ = TwoLinkedList()
    head = create_nodes(1)
    list_.add_to_head(head)
    node = list_.remove_from_tail()
    assert list_.is_empty()
    assert head == node


def test_two_linked_list_remove_from_tail():
    list_ = create_two_linked_list(node_count=6)
    old_array = list_.convert_to_array()
    old_tail = list_.get_tail()
    old_tail_prev = old_tail.get_prev()
    node = list_.remove_from_tail()
    new_array = list_.convert_to_array()
    assert len(list_) == 5
    assert old_tail == node
    assert old_array[:-1] == new_array
    assert list_.get_tail() == old_tail_prev
    assert old_tail_prev.get_next() is None


def test_two_linked_list_remove_by_value():
    nodes = [Node(100), Node(200), Node(100), Node(300), Node(100)]
    list_nodes = nodes[::-1]
    list_ = TwoLinkedList()
    for node in nodes:
        list_.add_to_head(node)

    list_.remove(value=100)
    del list_nodes[0]
    assert list_.convert_to_array() == list_nodes
    assert list_nodes[0] == list_.get_head()
    assert list_.get_head().get_prev() is None

    list_.remove(value=200)
    del list_nodes[2]
    assert list_.convert_to_array() == list_nodes


def test_two_linked_list_remove_by_value_all():
    nodes = [Node(100), Node(200), Node(100), Node(300), Node(100)]
    list_nodes = nodes[::-1]
    list_ = TwoLinkedList()
    for node in nodes:
        list_.add_to_head(node)

    list_.remove(value=100, is_all=True)
    expected = [node for node in list_nodes if node.get_value() != 100]
    assert list_.convert_to_array() == expected
    assert len(list_) == 2
    head, tail = list_nodes[1], list_nodes[-2]
    assert list_.get_head() == head
    assert list_.get_tail() == tail


def test_two_linked_list_reverse():
    list_ = create_two_linked_list(node_count=6)
    old_array = list_.convert_to_array()
    expected = old_array[::-1]
    list_.reverse()
    assert list_.convert_to_array() == expected
    assert list_.get_tail() == expected[-1]
    assert list_.get_head() == expected[0]
    assert list_.get_head().get_prev() is None
    assert list_.get_tail().get_next() is None


def test_linked_list_find():
    list_ = create_two_linked_list(node_count=6)
    assert bool(list_.find(value=100))
    assert list_.find(value=200) is None


def test_linked_list_find_all():
    nodes = [Node(100), Node(200), Node(100), Node(300), Node(100)]
    list_ = TwoLinkedList()
    for node in nodes:
        list_.add_to_head(node)

    expected = [node for node in nodes[::-1] if node.get_value() == 100]
    assert list_.find_all(value=100) == expected
