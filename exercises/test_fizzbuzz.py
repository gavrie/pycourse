"""
FizzBuzz:

Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five,
print "FizzBuzz".
"""
from fizzbuzz import calc_fizzbuzz

def test_fizzbuzz_number():
    assert calc_fizzbuzz(2) == '2'

def test_fizzbuzz_fizz():
    assert calc_fizzbuzz(3) == 'Fizz'

def test_fizzbuzz_buzz():
    assert calc_fizzbuzz(5) == 'Buzz'

def test_fizzbuzz_fizzbuzz():
    assert calc_fizzbuzz(15) == 'FizzBuzz'
