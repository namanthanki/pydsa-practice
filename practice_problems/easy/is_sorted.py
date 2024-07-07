import sys
sys.path.append('../../')
from data_structures.array import Array

def is_sorted(arr: Array) -> bool:
    for i in range(len(arr) - 1):
        if arr.get(i) > arr.get(i + 1):
            return False
    return True

def test_is_sorted():
    arr = Array(5)
    for i in range(5):
        arr.insert(i, i + 1)
    
    assert is_sorted(arr) == True
    print("Array: ", arr.__str__())
    print("Is sorted: ", is_sorted(arr))
    
    arr.insert(2, 10)
    assert is_sorted(arr) == False
    print("Array: ", arr.__str__())
    print("Is sorted: ", is_sorted(arr))
    
    arr.delete(2)
    assert is_sorted(arr) == True
    print("Array: ", arr.__str__())
    print("Is sorted: ", is_sorted(arr))
    
test_is_sorted()