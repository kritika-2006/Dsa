"""def countdown(n):
    # base class
    if n  <= 0:
        return
    countdown(n -1)
    print(n)
countdown(3)"""

def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n - 1)

countdown(3)