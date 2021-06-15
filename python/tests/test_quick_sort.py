from code_challenges.quick_sort.quick_sort import QuickSort, Partition, Swap

def test_unsorted_list():
    actual = QuickSort([1,5,6,7,8,2,4,55,111],0,8)
    expect = [1, 2, 4, 5, 6, 7, 8, 55, 111]
    assert actual == expect

def test_reverse_sorted():
    actual = QuickSort([20,18,12,8,5,-2],0,5)
    expect = [-2,5,8,12,18,20]
    assert actual == expect

def test_few_uniques():
    actual = QuickSort([5,12,7,5,5,7],0,5)
    expect = [5,5,5,7,7,12]
    assert actual == expect

def test_nearly_sorted():
    actual = QuickSort([2,3,5,7,13,11],0,5)
    expect = [2,3,5,7,11,13]
    assert actual == expect

def test_empty_list():
    actual = QuickSort([], 0, -1)
    expect = []
    assert actual == expect
