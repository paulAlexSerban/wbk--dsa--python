from min_stack import MinStack


def test_min_stack():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2


def test_min_stack_empty():
    min_stack = MinStack()
    assert min_stack.top() is None
    assert min_stack.getMin() is None


def test_min_stack_single_element():
    min_stack = MinStack()
    min_stack.push(42)
    assert min_stack.top() == 42
    assert min_stack.getMin() == 42
    min_stack.pop()
    assert min_stack.top() is None
    assert min_stack.getMin() is None


def test_min_stack_negative_numbers():
    min_stack = MinStack()
    min_stack.push(-5)
    min_stack.push(-2)
    min_stack.push(-8)
    assert min_stack.getMin() == -8
    min_stack.pop()
    assert min_stack.getMin() == -5
