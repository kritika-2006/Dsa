def count_digits(n):
    count = 0
    while n > 0:
        n  =  n // 10
        count = count + 1
    return count
print(count_digits(789))