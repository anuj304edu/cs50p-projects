from fuel import convert, gauge
import pytest

def test_1():
    assert convert("1/50") == 2

def test_2():
    assert gauge(99) == "F"

def test_3():
    assert gauge(1) == "E"

def test_4():
    assert gauge(45) == "45%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_match():
    with pytest.raises(ValueError):
        convert("10/4")