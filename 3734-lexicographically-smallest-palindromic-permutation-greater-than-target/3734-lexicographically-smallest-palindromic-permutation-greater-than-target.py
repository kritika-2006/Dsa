class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half_len = n // 2
        count = Counter(s)
        
        # Check if valid palindrome can be formed
        odd_chars = [ch for ch, cnt in count.items() if cnt % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Half characters pool
        half_counts = Counter()
        for ch, cnt in count.items():
            half_counts[ch] = cnt // 2
            
        # Target's first half and middle character
        target_half = target[:half_len]
        target_mid = target[half_len] if n % 2 != 0 else ""
        
        # Helper to reconstruct full palindrome
        def build_palindrome(half_str):
            rev_half = half_str[::-1]
            return half_str + mid_char + rev_half

        # Try to match prefix of target's first half of length i
        for i in range(half_len, -1, -1):
            curr_counts = half_counts.copy()
            prefix = []
            possible = True
            
            for j in range(i):
                ch = target_half[j]
                if curr_counts[ch] > 0:
                    curr_counts[ch] -= 1
                    prefix.append(ch)
                else:
                    possible = False
                    break
            
            if not possible:
                continue
                
            prefix_str = "".join(prefix)
            
            # Case 1: i == half_len (First half matches target_half exactly)
            if i == half_len:
                full_pal = build_palindrome(prefix_str)
                if full_pal > target:
                    return full_pal
                continue
                
            # Case 2: i < half_len (Choose next character strictly greater than target_half[i])
            target_ch = target_half[i]
            valid_next = sorted([ch for ch in curr_counts if curr_counts[ch] > 0 and ch > target_ch])
            
            if valid_next:
                next_ch = valid_next[0]
                curr_counts[next_ch] -= 1
                
                # Fill the rest of half with smallest available characters
                rem_half = []
                for ch in sorted(curr_counts.keys()):
                    rem_half.extend([ch] * curr_counts[ch])
                    
                full_half = prefix_str + next_ch + "".join(rem_half)
                return build_palindrome(full_half)
                
        return ""