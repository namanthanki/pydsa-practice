from typing import Any, Optional
import sys
sys.path.append("../../")
from data_structures.linked_list import LinkedList
from data_structures.linked_list import Node

class Stack:
    def __init__(self) -> None:
        self.linked_list: LinkedList = LinkedList()
        self.top: Optional[Node] = None
    
    def push(self, value: Any) -> None:
        self.linked_list.insert_at_beginning(value)
        self.top = self.linked_list.head
    
    def pop(self) -> Any:
        if self.is_empty():
            raise Exception("Stack is empty")
        
        if self.top is None:
            raise Exception("Unexpected error: top is None")
    
        popped_value = self.top.data
        self.linked_list.delete(self.top.data)
        self.top = self.linked_list.head
        return popped_value
    
    def is_empty(self) -> bool:
        return self.top is None
    
    def __str__(self) -> str:
        return self.linked_list.__str__()
    
def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    assert stack.__str__() == '[5, 4, 3, 2, 1]'
    assert stack.is_empty() == False
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() == True
    print("Stack tests pass")
    
test_stack()
    
    