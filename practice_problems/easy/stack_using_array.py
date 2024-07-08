import sys
sys.path.append("../../")
from data_structures.array import Array

class Stack:
    def __init__(self, capacity: int) -> None:
        self.arr = Array(capacity)
        self.top = -1
        self.capacity = capacity
    
    def push(self, value: int) -> None:
        if self.is_full():
            raise Exception("Stack is full")
        self.top += 1
        self.arr.insert(self.top, value)
        
    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.arr.get(self.top)
        self.top -= 1
        return value
    
    def peek(self) -> int:
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.arr.get(self.top)
    
    def is_empty(self) -> bool:
        return self.top == -1
    
    def is_full(self) -> bool:
        return self.top == self.capacity - 1
    
    def __str__(self) -> str:
        return self.arr.__str__()
    
def test_stack():
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    assert stack.__str__() == '[1, 2, 3, 4, 5]'
    assert stack.is_full() == True
    assert stack.is_empty() == False
    assert stack.peek() == 5
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() == True
    assert stack.is_full() == False
    print("Stack tests pass")
    
test_stack()
