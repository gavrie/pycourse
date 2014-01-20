def average(numbers):
    total = 0
    length = 0

    for n in numbers:
        total = total + n
        length = length + 1

    return 1.0 * total / length


grades = [80, 20, 70, 30, 90, 95, 100, 78]
print average(grades)
