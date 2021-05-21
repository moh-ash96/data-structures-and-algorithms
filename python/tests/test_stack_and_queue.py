from Data_Structures.stacks_and_queues.stacks_and_queues import Node, Stack, Queue
import pytest

stack = Stack()

def test_push():
    stack.push('5')
    actual = stack.top.value
    expect = '5'
    assert actual == expect


def test_multi_values():
    stack.push('hi')
    actual = stack.__str__()
    expect = 'hi\n5'
    assert actual == expect

def test_pop():
    assert stack.pop() == 'hi'
    actual = stack.__str__()
    expect = '5'
    assert actual == expect


def test_multi_pop():
    stack.push('m')
    stack.push('o')
    stack.push('h')
    assert stack.__str__() == 'h\no\nm\n5'
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.__str__() == ''

def test_peek():
    stack.push('m')
    stack.push('o')
    stack.push('h')
    assert stack.peek() == 'h'

def test_initiate_empty_stack():
    stack2 = Stack()
    assert stack2.__str__() == ''

def test_pop_and_peek_on_empty():
    stack3 = Stack()
    assert stack3.pop() == 'Cannot pop from empty stack'
    assert stack3.peek() == 'Cannot peek from empty stack'


queue = Queue()

def test_enqueue():
    queue.enqueue('m')
    assert queue.__str__() == 'm'

def test_enqueue_multiple_values():
    queue.enqueue('o')
    assert queue.__str__() == 'm\no'

def test_dequeue():

    assert queue.dequeue() == 'm'
    assert queue.__str__() == 'o'

def test_peek_queue():
    queue.enqueue('m')
    queue.enqueue('a')
    queue.enqueue('r')
    assert queue.peek() == ('o')

def test_multiple_dequeue():
    assert queue.__str__() == 'o\nm\na\nr'
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.__str__() == ''

def test_init_queue():
    queue2 = Queue()
    assert queue2.__str__() == ''

def test_peek_empty_queue():
    empty_queue = Queue()
    assert empty_queue.__str__() == ''
    assert empty_queue.peek() == 'Cannot peek from empty queue'
