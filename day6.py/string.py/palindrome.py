def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        elif s[left] == s[right]:
            left = left + 1
            right = right - 1
    return True

print(is_palindrome("nitin"))
print(is_palindrome("kritika"))
        