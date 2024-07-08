from typing import Any, Optional

class Node:
    def __init__(self, data: Any, next: Optional["Node"] = None) -> None:
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
    
    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def insert_at_beginning(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_position(self, data: Any, position: int) -> None:
        if position < 0:
            raise ValueError("Position cannot be negative")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current_node = self.head
        counter = 0
        while current_node and counter < position - 1:
            current_node = current_node.next
            counter += 1
        
        if current_node is None:
            raise ValueError("Position out of bounds")
        
        new_node.next = current_node.next
        current_node.next = new_node
        
    def delete(self, data: Any) -> None:
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
    
    def __str__(self) -> str:
        if self.head is None:
            return '[]'
        
        result = '['
        current_node = self.head
        while current_node:
            result += str(current_node.data) + ', '
            current_node = current_node.next
        return result[:-2] + ']'
    
def test_linked_list() -> None:
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    assert linked_list.__str__() == '[1, 2, 3, 4, 5]'
    
    linked_list.insert_at_beginning(0)
    assert linked_list.__str__() == '[0, 1, 2, 3, 4, 5]'
    
    linked_list.insert_at_position(10, 3)
    assert linked_list.__str__() == '[0, 1, 2, 10, 3, 4, 5]'
    
    linked_list.delete(10)
    assert linked_list.__str__() == '[0, 1, 2, 3, 4, 5]'
    
    linked_list.delete(0)
    assert linked_list.__str__() == '[1, 2, 3, 4, 5]'
    
    linked_list.delete(5)
    assert linked_list.__str__() == '[1, 2, 3, 4]'
    
    print("Linked list tests pass")
    
# test_linked_list()

__all__ = ["LinkedList", "Node"]