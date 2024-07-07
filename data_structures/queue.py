from typing import Any

class Queue:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.length = 0
        self.data: list[Any] = [None] * capacity
        self.front = 0
        self.rear = 0
    
    def resize(self, new_capacity: int) -> None:
        new_data: list[Any] = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[(self.front + i) % self.capacity]
        self.data = new_data
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.length
    
    def enqueue(self, value: Any) -> None:
        if self.length == self.capacity:
            self.resize(self.capacity * 2)
        
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.length += 1
    
    def dequeue(self) -> Any:
        if self.length == 0:
            raise IndexError('Queue underflow')
        item = self.data[self.front]
        self.front = (self.front + 1) % self.capacity
        self.length -= 1
        if self.length <= self.capacity // 4:
            self.resize(self.capacity // 2)
        return item
    
    def peek(self) -> Any:
        if self.length == 0:
            raise IndexError('Queue underflow')
        return self.data[self.front]
    
    def __str__(self) -> str:
        return str(self.data[:self.length])
    
    def __len__(self) -> int:
        return self.length
    
def test_queue():
    queue = Queue(5)
    for i in range(5):
        queue.enqueue(i + 1)
    
    assert queue.__str__() == '[1, 2, 3, 4, 5]'
    print(queue.__str__())
    
    queue.enqueue(10)
    assert queue.__str__() == '[1, 2, 3, 4, 5, 10]'
    print(queue.__str__())
    
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print(queue.__str__())
    
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    
    assert queue.__str__() == '[]'
    
    try:
        queue.dequeue()
    except IndexError as e:
        assert str(e) == 'Queue underflow'
        print(str(e))
        
test_queue()
        