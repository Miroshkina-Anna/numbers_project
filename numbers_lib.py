def sum_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
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
    num = []
    while number > 0:
        digit = number % 10
        num.append(digit)
        number //= 10
    maximum = max(num)
    print(maximum)
    return maximum

max_digit(123)

def min_digit(number):
    num = []
    while number > 0:
        digit = number % 10
        num.append(digit)
        number //=10
    minimum = min(num)
    print(minimum)
    return minimum

min_digit(123)

def is_even(number):
    if number % 2 == 0:
        print("является четным")
        return "even"
    else:
        print("является нечетным")
        return "odd"

is_even(123)

def multiply_digits(number):
    prod = 1
    while number > 0:
        digit = number % 10
        prod *= digit
        number //= 10
    print(prod)
    return prod
multiply_digits(123)

def reverse_number(number):
    num = []
    while number > 0:
        digit = number % 10
        num.append(str(digit))
        number //= 10
    result = "".join(num)
    print(result)

reverse_number(1245)





