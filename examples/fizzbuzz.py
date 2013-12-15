def fizzbuzz():
    for i in range(1, 101):
        print calc_fizzbuzz(i)

def calc_fizzbuzz(i):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"

    if not output:
        output += str(i)
    return output

# fizzbuzz()
print calc_fizzbuzz(2)
print calc_fizzbuzz(3)
print calc_fizzbuzz(5)
print calc_fizzbuzz(15)
