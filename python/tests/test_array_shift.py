import pytest

from code_challenges.array_shift.array_shift import insertShiftArray

def test1():
    actual = insertShiftArray([1, 2, 3, 4],5)
    expected = [1, 2, 5, 3, 4]
    assert actual == expected

def test2():
    actual = insertShiftArray([5, 5, 5, 5, 5, 5], 4)
    expected = [5,5,5,4,5,5,5]
    assert actual == expected

def test3():
    actual = insertShiftArray([10, 20, 30],60)
    expected = [10,60,20,30]
    assert actual == expected

def test4():
    actual = insertShiftArray([1], 2)
    expected = [1, 2]
    assert actual == expected
