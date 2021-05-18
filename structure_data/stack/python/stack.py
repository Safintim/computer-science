class Stack:
    def __init__(self) -> None:
        self.data = []

    def push(self, value) -> None:
        self.data.append(value)

    def pop(self) -> None:
        self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def is_empty(self) -> bool:
        return bool(self.data)


class MinStack:
    def __init__(self) -> None:
        self.data = []

    def push(self, value) -> None:
        minimum = self.get_min()
        if minimum is None or minimum > value:
            minimum = value
        self.data.append((value, minimum))

    def pop(self) -> None:
        self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1][0]

    def get_min(self):
        if self.data:
            return self.data[-1][1]