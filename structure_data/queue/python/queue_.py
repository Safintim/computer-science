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
