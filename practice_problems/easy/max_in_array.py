import sys
sys.path.append('../../')
from data_structures.array import Array

def max_in_array(arr: Array) -> int:
    max_val = arr.get(0)
    for i in range(len(arr)):
        if arr.get(i) > max_val:
            max_val = arr.get(i)

    return max_val

def test_max_in_array():
    arr = Array(5)
    for i in range(5):
        arr.insert(i, i - i - 1 - i)
    
    print(arr.__str__())
    
    max = max_in_array(arr)
    assert max == -1
    print("Array: ", arr.__str__())
    print("Max in array: ", max)

    arr.insert(2, 10)
    max = max_in_array(arr)
    assert max == 10
    print("Array: ", arr.__str__())
    print("Max in array: ", max)

    arr.delete(2)
    max = max_in_array(arr)
    assert max == -1
    print("Array: ", arr.__str__())
    print("Max in array: ", max)
    
test_max_in_array()