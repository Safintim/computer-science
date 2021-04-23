from queue_ import Queue


def test_create_queue():
    q = Queue(5)
    assert q.is_empty()
    assert not q.is_full()


def test_enqueue():
    q = Queue(3)
    index_head = 0
    index_tail = 2
    assert q.enqueue(1)
    assert q.enqueue(2)
    assert q.enqueue(3)
    assert not q.enqueue(4)
    assert not q.is_empty()
    assert q.is_full()
    assert q.head == index_head
    assert q.tail == index_tail


def test_dequeue():
    q = Queue(3)
    for val in range(1, 4):
        q.enqueue(val)

    index_head = index_tail = -1
    assert q.is_full()
    assert q.dequeue()
    assert q.dequeue()
    assert q.dequeue()
    assert q.is_empty()
    assert q.head == index_head
    assert q.tail == index_tail


def test_enqueue_dequeue():
    q = Queue(3)
    for val in range(1, 4):
        q.enqueue(val)

    assert q.front() == 1
    assert q.rear() == 3

    assert q.dequeue()
    assert q.front() == 2
    assert q.rear() == 3

    assert q.dequeue()
    assert q.front() == 3

    assert q.enqueue(10)
    assert q.rear() == 10


def test_work():
    q = Queue(3)
    assert q.enqueue(7)
    assert q.dequeue()
    assert q.front() == -1
    assert not q.dequeue()
    assert q.front() == -1
    assert q.rear() == -1
    assert q.enqueue(0)
    assert not q.is_full()
    assert q.dequeue()
    assert q.enqueue(3)
    assert q.enqueue(4)
    assert q.enqueue(5)
    assert q.is_full()
    assert q.front() == 3
    assert q.rear() == 5
