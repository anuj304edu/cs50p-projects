from plates import is_valid

def test_is_valid():
    assert is_valid("anuj20") == True

def test_number():
    assert is_valid("20anuj") == False

def test_punctuation():
    assert is_valid("an$o2") == False

def test_space():
    assert is_valid("an u02") == False

def test_first_number():
    assert is_valid("anuj02") == False

def test_middle_number():
    assert is_valid("an33ujp") == False

def test_length():
    assert is_valid("anujp") == True

def test_alpha():
    assert is_valid("an") == True
