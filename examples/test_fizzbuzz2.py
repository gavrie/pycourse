from fizzbuzz2 import calc_fizzbuzz

def test_fizzbuzz_number():
    assert calc_fizzbuzz(2) == '2'

def test_fizzbuzz_fizz():
    assert calc_fizzbuzz(3) == 'Fizz'

def test_fizzbuzz_buzz():
    assert calc_fizzbuzz(5) == 'Buzz'

def test_fizzbuzz_fizzbuzz():
    assert calc_fizzbuzz(15) == 'FizzBuzz'
