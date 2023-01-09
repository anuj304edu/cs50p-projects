from working import convert
import pytest

def test_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_3():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_4():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_valueerror():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_VE():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_VE2():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_VE3():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00 ")