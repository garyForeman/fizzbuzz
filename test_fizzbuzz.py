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


def test_four():
    fb = FizzBuzz()
    assert fb.parse(4) == 4


def test_five():
    fb = FizzBuzz()
    assert fb.parse(5) == 'buzz'


def test_six():
    fb = FizzBuzz()
    assert fb.parse(6) == 'fizz'


def test_ten():
    fb = FizzBuzz()
    assert fb.parse(10) == 'buzz'


def test_fifteen():
    fb = FizzBuzz()
    assert fb.parse(15) == 'fizzbuzz'


def test_thirty():
    fb = FizzBuzz()
    assert fb.parse(30) == 'fizzbuzz'
