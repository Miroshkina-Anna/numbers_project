def sum_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    print(sum)
    return sum
sum_digits(123)

def count_digits(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    print(count)
    return count
count_digits(123)

def max_digit(number):
    numbers = []
    while number > 0:
        num = number % 10
        numbers.append(num)
        number //= 10
    maximum = max(numbers)
    print(maximum)
    return maximum
max_digit(123)

def min_digit(number):
    numbers = []
    while number > 0:
        num = number % 10
        numbers.append(num)
        number //= 10
    minimum = min(numbers)
    print(minimum)
    return minimum
max_digit(123)