from bank import value


def test_value():
    assert value("Hello") == 0

def test_value2():
    assert value("hii") == 20

def test_number():
    assert value("123Hello") == 100

def test_punctuation():
    assert value("$Hello") == 100