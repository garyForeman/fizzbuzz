from fizzbuzz import FizzBuzz


def test_one():
    fb = FizzBuzz()
    assert fb.parse(1) == 1


def test_two():
    fb = FizzBuzz()
    assert fb.parse(2) == 2


def test_three():
    fb = FizzBuzz()
    assert fb.parse(3) == 'fizz'


def test_six():
    fb = FizzBuzz()
    assert fb.parse(6) == 'fizz'