from Data_Structures.stacks_and_queues.stacks_and_queues import Node, Stack, Queue
import pytest

stack = Stack()

def test_push():
    stack.push('5')
    actual = stack.top.value
    expect = '5'
    assert actual == expect

@pytest.mark.skip
def test_multi_values():
    stack.push('hi')
    actual = stack.__str__()
    expect = ['5', 'hi']
    assert actual == expect
