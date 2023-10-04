import math
def test_grade():
    g = 50
    assert g >= 50

def test_convertion():
    celsius = 0
    F = celsius * (9/5) + 32
    assert F == 32

def test_area():
    side = 5
    a = side * side
    assert a == 25