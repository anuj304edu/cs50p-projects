from seasons import get_days, get_minutes
import pytest

def test_1():
    assert get_minutes("2002-02-24") == 10926720

def test_2():
    assert get_minutes("2022-12-01") == 4320

