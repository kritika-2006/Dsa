def is_palindrome(n):
    left = 0
    right = len(n) - 1
    result =  0
    while left < right:
        if n[left] == n[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
n = ("nitin")
print("check:", is_palindrome(n))