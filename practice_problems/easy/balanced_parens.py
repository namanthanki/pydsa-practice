import sys
sys.path.append("../../")
from data_structures.stack import Stack

def balanced_parens(string):
    stack = Stack()
    for char in string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
        

def test_balanced_parens():
    assert balanced_parens('()') == True
    assert balanced_parens(')(') == False
    assert balanced_parens('()()') == True
    assert balanced_parens('((()))') == True
    assert balanced_parens('(()()())') == True
    assert balanced_parens('(()()())(') == False
    assert balanced_parens(')()()(') == False
    assert balanced_parens(')()()()') == False
    assert balanced_parens('()()()') == True
    assert balanced_parens('()()()(') == False
    assert balanced_parens('()()()()') == True
    assert balanced_parens('()()()()(') == False
    assert balanced_parens('()()()()()') == True
    assert balanced_parens('()()()()()(') == False
    assert balanced_parens('()()()()()()') == True
    assert balanced_parens('()()()()()()(') == False
    assert balanced_parens('()()()()()()()') == True
    assert balanced_parens('()()()()()()()(') == False
    assert balanced_parens('()()()()()()()()') == True
    assert balanced_parens('()()()()()()()()(') == False
    assert balanced_parens('()()()()()()()()()') == True
    assert balanced_parens('()()()()()()()()()(') == False
    
    print('All tests passed')
    
test_balanced_parens()