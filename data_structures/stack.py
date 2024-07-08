from typing import Any

class Stack:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.length = 0
        self.data: list[Any] = [None] * capacity
        
    def resize(self, new_capacity: int) -> None:
        if new_capacity < 1:
            new_capacity = 1
        new_data: list[Any] = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
        self.length = min(self.length, self.capacity)
    
    def push(self, value: Any) -> None:
        if self.is_full():
            self.resize(self.capacity * 2)
        self.data[self.length] = value
        self.length += 1
        
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('Stack underflow')
        item = self.data[self.length - 1]
        self.length -= 1
        if self.length <= self.capacity // 4:
            self.resize(self.capacity // 2)
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError('Stack underflow')
        return self.data[self.length - 1]
    
    def is_empty(self) -> bool:
        return self.length == 0
    
    def is_full(self) -> bool:
        return self.length == self.capacity
    
    def __str__(self) -> str:
        return str(self.data[:self.length])
    
    def __len__(self) -> int:
        return self.length
    
def test_stack():
    stack = Stack(5)
    for i in range(5):
        stack.push(i + 1)
    
    assert stack.__str__() == '[1, 2, 3, 4, 5]'
    print(stack.__str__())
    
    stack.push(10)
    assert stack.__str__() == '[1, 2, 3, 4, 5, 10]'
    print(stack.__str__())
    
    stack.pop()
    stack.pop()
    assert stack.__str__() == '[1, 2, 3, 4]'
    print(stack.__str__())
    
    assert stack.peek() == 4
    print(stack.peek())
    
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.__str__() == '[]'
    print(stack.__str__())
    
    try:
        stack.pop()
    except IndexError as e:
        assert str(e) == 'Stack underflow'
        print(str(e))
    
# test_stack()