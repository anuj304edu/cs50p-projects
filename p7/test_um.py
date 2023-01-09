from um import count
import pytest

def test_1():
    assert count("Um, thanks, um...") == 2

def test_2():
    assert count("my name is um?") == 1

def test_3():
    assert count("10 uum to 8 um") == 1

def test_4():
    assert count("my name is anuj") == 0

