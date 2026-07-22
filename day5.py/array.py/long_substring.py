def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        #Agar right wala character pehle se set me hai, left se hatao
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
            # Naye character ko set me daalo
        seen.add(s[right])
           # Max length update karo
        current_len = right - left + 1
        max_len = max(max_len, current_len)
    return max_len
print(lengthOfLongestSubstring("abcabcbb"))