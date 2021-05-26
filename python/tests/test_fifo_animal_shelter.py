from code_challenges.fifo_animal_shelter.fifo_animal_shelter import *
import pytest

shell = AnimalShelter()

def test_enqueue():
    shell.enqueue('cat')
    shell.enqueue('dog')
    assert shell.__str__() == 'cat\ndog'
    shell.enqueue('bird')
    assert shell.__str__() == 'cat\ndog'
    shell.enqueue('cat')
    shell.enqueue('cat')
    shell.enqueue('dog')
    assert shell.__str__() == 'cat\ndog\ncat\ncat\ndog'


def test_dequeue():
    assert shell.dequeue('dog') == 'dog'
    assert shell.__str__() == 'cat\ncat\ncat\ndog'
    assert shell.dequeue('bird') == None
