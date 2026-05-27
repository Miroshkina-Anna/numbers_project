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