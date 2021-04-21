from typing import Union, List
from two_linked_list import Node, TwoLinkedList


def create_nodes(
    count: int,
    start_value: int = 100
) -> Union[List[Node], Node]:
    if count == 1:
        return Node(start_value)
    return [Node(start_value + i) for i in range(count)]


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
    #error
    list_ = TwoLinkedList()
    node1 = create_nodes(1)
    list_.init(node1)

    node2 = create_nodes(1)
    list_.add_to_tail(node2)
    assert list_.get_tail() == node2
    assert list_.get_tail().get_prev() == node2


# def test_two_linked_list_insert():
#     list_1 = TwoLinkedList()
#     list_1.insert(node)
