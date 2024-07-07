import sys
sys.path.append('../../')
from data_structures.array import Array

def reverse_array(arr: Array) -> None:
    length = len(arr)
    for i in range(length // 2):
        temp = arr.get(i)
        arr.set(i, arr.get(length - 1 - i))
        arr.set(length - 1 - i, temp)
        
def test_reverse_array():
    arr = Array(5)
    for i in range(5):
        arr.insert(i, i + 1)
    
    print(arr.__str__())
    
    reverse_array(arr)
    assert arr.__str__() == '[5, 4, 3, 2, 1]'
    print(arr.__str__())
    
    arr.insert(2, 10)
    reverse_array(arr)
    assert arr.__str__() == '[1, 2, 3, 10, 4, 5]'
    print(arr.__str__())
    
    arr.delete(2)
    reverse_array(arr)
    assert arr.__str__() == '[5, 4, 10, 2, 1]'
    print(arr.__str__())

test_reverse_array()