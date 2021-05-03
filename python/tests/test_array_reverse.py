from code_challenges.array_reverse.array_reverse import reverseArray

def test_array ():
    assert reverseArray([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]
    assert reverseArray([89, 2354, 3546, 23, 10, -923, 823, -12]) == [-12, 823, -923, 10, 23, 3546, 2354, 89]
