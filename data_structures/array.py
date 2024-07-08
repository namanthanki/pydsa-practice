from typing import Any

class Array:
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

    def insert(self, index: int, value: Any) -> None:
        if self.length == self.capacity:
            self.resize(self.capacity * 2)
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.length += 1

    def delete(self, index: int) -> Any:
        if index < 0 or index >= self.length:
            raise IndexError('Index out of bounds')
        item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self.length -= 1
        if self.length <= self.capacity // 4:
            self.resize(self.capacity // 2)
        return item

    def get(self, index: int) -> Any:
        return self.data[index]

    def set(self, index: int, value: Any) -> None:
        self.data[index] = value

    def __str__(self) -> str:
        return str(self.data[:self.length])

    def __len__(self) -> int:
        return self.length

    
def test_array():
    arr = Array(5)
    for i in range(5):
        arr.insert(i, i + 1)
    
    assert arr.__str__() == '[1, 2, 3, 4, 5]'
    print(arr.__str__())
    
    arr.insert(2, 10)
    assert arr.__str__() == '[1, 2, 10, 3, 4, 5]'
    print(arr.__str__())
    
    arr.delete(2)
    assert arr.__str__() == '[1, 2, 3, 4, 5]'
    print(arr.__str__())
    
# test_array()        

__all__ = ['Array']