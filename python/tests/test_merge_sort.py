from code_challenges.merge_sort.merge_sort import merge_sort, merge

def test_unsorted_list():
    actual = merge_sort([1,5,6,7,8,2,4,55,111])
    expect = [1, 2, 4, 5, 6, 7, 8, 55, 111]
    assert actual == expect

def test_reverse_sorted():
    actual = merge_sort([20,18,12,8,5,-2])
    expect = [-2,5,8,12,18,20]
    assert actual == expect

def test_few_uniques():
    actual = merge_sort([5,12,7,5,5,7])
    expect = [5,5,5,7,7,12]
    assert actual == expect

def test_nearly_sorted():
    actual = merge_sort([2,3,5,7,13,11])
    expect = [2,3,5,7,11,13]
    assert actual == expect

