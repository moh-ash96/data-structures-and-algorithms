from code_challenges.left_join.left_join import left_join
from code_challenges.left_join.hashtable import Hashtable
import pytest


def test_join_left_all_the_same(hash):
    actual = left_join(hash[0], hash[1])
    expected = [
        ["fond", "enamored", "averse"],
        ["wrath", "anger", "delight"],
        ["diligent", "employer", "idle"],
        ["outfit", "garb", None],
        ["guide", "usher", "follow"],
    ]
    assert actual == expected


def test_no_matches(hash):
    actual = left_join(hash[2], hash[3])
    expected = [
        ["rich", "wealthy", None],
        ["good", "nice", None],
        ["long", "tall", None],
        ["happy", "amused", None],
    ]
    assert actual == expected


def test_one_is_empty(hash):
    actual = left_join(hash[4], hash[5])
    expected = [
        ["fond", "enamored", None],
        ["wrath", "anger", None],
        ["diligent", "employer", None],
        ["outfit", "garb", None],
        ["guide", "usher", None],
    ]
    assert actual == expected


@pytest.fixture
def hash():
    hash1 = Hashtable()
    hash2 = Hashtable()

    hash3 = Hashtable()
    hash4 = Hashtable()

    hash5 = Hashtable()
    hash6 = Hashtable()

    hash1.add("fond", "enamored")
    hash1.add("wrath", "anger")
    hash1.add("diligent", "employer")
    hash1.add("outfit", "garb")
    hash1.add("guide", "usher")

    hash2.add("fond", "averse")
    hash2.add("wrath", "delight")
    hash2.add("diligent", "idle")
    hash2.add("guide", "follow")
    hash2.add("flow", "jam")

    hash3.add("rich", "wealthy")
    hash3.add("good", "nice")
    hash3.add("long", "tall")
    hash3.add("happy", "amused")

    hash4.add("fond", "averse")
    hash4.add("wrath", "delight")
    hash4.add("diligent", "idle")
    hash4.add("guide", "follow")
    hash4.add("flow", "jam")

    hash5.add("fond", "enamored")
    hash5.add("wrath", "anger")
    hash5.add("diligent", "employer")
    hash5.add("outfit", "garb")
    hash5.add("guide", "usher")

    # hash6.add('fond', 'averse')
    # hash6.add('wrath', 'delight')
    # hash6.add('diligent', 'idle')
    # hash6.add('guide', 'follow')
    # hash6.add('flow', 'jam')

    return [hash1, hash2, hash3, hash4, hash5, hash6]
