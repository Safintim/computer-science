from queue import Queue as PythonQueue


class Queue:
    def __init__(self, max_size) -> None:
        self.max_size: int = max_size
        self.data = [None] * max_size
        self.head: int = -1
        self.tail: int = -1

    def is_empty(self) -> bool:
        return self.head == -1

    def is_full(self) -> bool:
        return ((self.tail + 1) % self.max_size) == self.head

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False

        if self.is_empty():
            self.head = 0

        self.tail = (self.tail + 1) % self.max_size
        self.data[self.tail] = value
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True

        self.head = (self.head + 1) % self.max_size
        return True

    def front(self) -> int:
        return -1 if self.is_empty() else self.data[self.head]

    def rear(self) -> int:
        return -1 if self.is_empty() else self.data[self.tail]


class MovingAverage:
    def __init__(self, size: int):
        self.queue = PythonQueue(maxsize=size)
        self.total = 0

    def next(self, value: int) -> float:
        if self.queue.full():
            self.total -= self.queue.get()

        self.queue.put(value)
        self.total += value
        return self.total / self.queue.qsize()


class QueueBaseStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack2.append(x)

    def pop(self):
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        return self.stack1.pop()

    def peek(self):
        if self.stack1:
            return self.stack1[-1]
        else:
            return self.stack2[0]

    def empty(self):
        return not (self.stack1 or self.stack2)
