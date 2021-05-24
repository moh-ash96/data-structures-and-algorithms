from code_challenges.queue_with_stacks.queue_with_stack import PseudoQueue

queue = PseudoQueue()

def test_enqueue():
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    queue.enqueue(20)
    assert queue.__str__() == "15\n10\n5\n20"
    queue2 = PseudoQueue()
    queue2.enqueue(5)
    assert queue2.__str__() == '5'

def test_dequeue():
    assert queue.dequeue() == '15'
    assert queue.dequeue() == '10'
    assert queue.__str__() == '5\n20'

