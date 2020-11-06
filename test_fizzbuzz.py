from fizzbuzz import FizzBuzz

def test_one():
    fb = FizzBuzz()
    assert fb.parse(1) == 1

def test_two():
    fb = FizzBuzz()
    assert fb.parse(2) == 2
