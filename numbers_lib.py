def sum_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    print(sum)
    return sum
sum_digits(123)