from typing import TypeVar, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def push(self, item: T):
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

# Usage
stack_of_ints = Stack[int]()
stack_of_ints.push(1)
stack_of_ints.push(2)
print(stack_of_ints.pop())  # Output: 2

stack_of_strs = Stack[str]()
stack_of_strs.push("hello")
stack_of_strs.push("world")
print(stack_of_strs.pop())  # Output: world
