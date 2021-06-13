from code_challenges.insertion_sort.insertion import selection_sort

def test_sort():
    actual = selection_sort([5,7,2,4,58,22])
    expect = [2,4,5,7,22,58]
    assert actual == expect

def test_negative():
    actual = selection_sort([5,-55,-1,8,6,10,20])
    expect = [-55,-1,5,6,8,10,20]
    assert actual == expect
