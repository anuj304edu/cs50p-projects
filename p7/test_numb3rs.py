import pytest
from numb3rs import validate

def test_1():
    assert validate("127.0.0.1") == True

def test_2():
    assert validate("127.0.1") == False

def test_3():
    assert validate("64.428.256.512") == False

def test_4():
    assert validate("127.0.01") == False
