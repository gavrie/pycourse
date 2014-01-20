"""
FizzBuzz:

Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five,
print "FizzBuzz".

To create your solution, you need to:

    1. Create a module named 'fizzbuzz.py'
    2. Write a function named 'calc_fizzbuzz' that works according to the tests.
    3. Run the test with the command 'py.test test_fizzbuzz.py'
    4. Change your code and repeat until the tests pass!
    5. Ensure your programs prints the values from 1 to 100 correctly,
       by running 'python fizzbuzz.py' and looking at the output.
"""
from fizzbuzz import calc_fizzbuzz

def test_fizzbuzz_number():
    assert calc_fizzbuzz(1) == '1'
    assert calc_fizzbuzz(2) == '2'
    assert calc_fizzbuzz(4) == '4'

def test_fizzbuzz_fizz():
    assert calc_fizzbuzz(3) == 'Fizz'
    assert calc_fizzbuzz(9) == 'Fizz'

def test_fizzbuzz_buzz():
    assert calc_fizzbuzz(5) == 'Buzz'
    assert calc_fizzbuzz(50) == 'Buzz'

def test_fizzbuzz_fizzbuzz():
    assert calc_fizzbuzz(15) == 'FizzBuzz'
    assert calc_fizzbuzz(45) == 'FizzBuzz'
