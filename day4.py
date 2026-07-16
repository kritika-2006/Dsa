def get_sum(n):
    # base class
    if n == 0:
        return 0
    # recursive relation
    return n + get_sum(n - 1)
print(get_sum(4))