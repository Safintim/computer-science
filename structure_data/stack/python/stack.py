import math
from collections import deque


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


def is_valid_parentheses(s):
    stack = []
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    for char in s:
        if char in brackets:
            stack.append(char)
        else:
            if not stack:
                return False
            bracket = stack.pop()
            if char != bracket:
                return False
    return not stack


def daily_temperature(temperatures):
    result = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            cur = stack.pop()
            result[cur] = i - cur
        stack.append(i)
    return result


def eval_reverse_polish_notation(self, tokens):
    operators = '+*/-'
    stack = []
    for token in tokens:
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                res = operand2 + operand1
            elif token == '-':
                res = operand1 - operand2
            elif token == '*':
                res = operand2 * operand1
            else:
                res = math.trunc(operand1 / operand2)
            stack.append(res)
        else:
            stack.append(int(token))
    return stack.pop()


class StackBasedOnQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        el = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return el

    def top(self):
        return self.q1[-1]

    def empty(self):
        return not (self.q1 or self.q2)
