def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]
numbers = [10, 25, 5, 40, 30]
print(second_largest(numbers))
