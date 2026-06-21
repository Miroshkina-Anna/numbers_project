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
    reversed_number = int(str(number)[::-1])
    print(reversed_number)
    return reversed_number
reverse_number(123)

def is_palindrome(number):
    digit = int(str(number)[::-1])
    if digit == number:
        print("является палиндромом")
        return "palindrome"
    else:
        print("не является палиндромом")
        return "not palindrome"

def count_even_digits(number):
    count = 0
    while number > 0:
        if (number % 10) % 2 == 0:
            count += 1
        number //= 10
    print(count)
    return count
count_even_digits(123)

def count_odd_digits(number):
    count = 0
    while number > 0:
        if (number % 10) % 2 != 0:
            count += 1
        number //= 10
    print(count)
    return count
count_odd_digits(123)

def first_digit(number):
    digit = int(str(number)[0])
    print(digit)
    return digit
first_digit(123)

def last_digit(number):
    digit = int(str(number)[-1])
    print(digit)
    return digit
last_digit(123)

def sum_even_digits(number):
    sum = 0
    while number > 0:
        if number % 2 == 0:
            sum += number % 10
        number //= 10
    print(sum)
    return sum
sum_even_digits(123)

def sum_odd_digits(number):
    sum = 0
    while number > 0:
        if number % 2 != 0:
            sum += number % 10
        number //= 10
    print(sum)
    return sum
sum_odd_digits(123)

def square_number(number):
    return number ** 2
print(square_number(11))

def cube_number(number):
    return number ** 3
print(cube_number(3))

