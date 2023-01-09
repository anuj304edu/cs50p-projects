from twttr import shorten

def test_shorten():
    assert shorten("Anuj") == "nj"

def test_shorte_n():
    assert shorten("Gautam ParimAr") == "Gtm Prmr"

def test_number():
    assert shorten("1212") == "1212"

def test_punctuation():
    assert shorten('!#$%&()*+, -./:;<=>?@[]^_`{|}~') == '!#$%&()*+, -./:;<=>?@[]^_`{|}~'