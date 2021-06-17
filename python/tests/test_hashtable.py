from Data_Structures.hashtable.hashtable import Hashtable
# import pytest

def test_add_key_value():
    hashtable = Hashtable()
    actual = hashtable.add("DOB","1996")
    expect = ["DOB", "1996"]
    assert actual == expect

def test_get_value():
    hashtable = Hashtable()
    hashtable.add('length', 174)
    actual = hashtable.get('length')
    expect = 174
    assert actual == expect

def test_get_none_value():
    hashtable = Hashtable()
    hashtable.add('length', 174)
    actual = hashtable.get('wight')
    expect = None
    assert actual == expect

def test_handle_collision():
    hashtable = Hashtable()
    hashtable.add('fall', 'to the ground')
    hashtable.add('fall', 'as in seasons')
    for bucket in hashtable._buckets:
        if bucket:
            actual = str(bucket)
    assert actual == "['fall', 'to the ground']->['fall', 'as in seasons']->None"


def test_retrive_collision():
    hashtable = Hashtable()
    hashtable.add("fried", "chicken")
    hashtable.add("fired", "the employee")
    actual = [hashtable.get("fried"), hashtable.get("fired")]
    expect = ["chicken", "the employee"]
    assert actual == expect

def test_contains():
    hashtable = Hashtable()
    hashtable.add("Hello", "It is me")
    actual = hashtable.contains('Hello')
    expected = True
    assert actual == expected

    actual2 = hashtable.contains("Where")
    expected2 = False
    assert actual2 == expected2

def test_hash_key_in_range():
    expected  = 1024
    hashtable = Hashtable()
    actual = hashtable._hash('house')
    assert actual in range(expected)
