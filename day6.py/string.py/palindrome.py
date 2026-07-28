def is_palindrome(s):
   # Clean the string (spaces/symbols remove + lowercase)
    s = [ch.lower() for ch in s if ch.isalnum()]
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        
        # s[left] == s[right]:
        else:
            left = left + 1
            right = right - 1
    return True

print(is_palindrome("nitin"))
print(is_palindrome("kritika"))
        