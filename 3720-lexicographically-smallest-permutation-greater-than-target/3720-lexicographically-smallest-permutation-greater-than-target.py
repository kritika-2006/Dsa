from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        n = len(target)
        
        def can_build(idx, current_counts):
            # Helper to check if remaining characters can form valid string
            rem_target = target[idx:]
            rem_chars = []
            for ch in sorted(current_counts.keys()):
                rem_chars.extend([ch] * current_counts[ch])
            rem_str = "".join(rem_chars)
            return rem_str >= rem_target

        ans = []
        
        # We try to match prefix with target, then break at index i by choosing a strictly larger character
        for i in range(n, -1, -1):
            prefix_counts = Counter(s)
            prefix = []
            possible = True
            
            # Try to match prefix target[:i]
            for j in range(i):
                ch = target[j]
                if prefix_counts[ch] > 0:
                    prefix_counts[ch] -= 1
                    prefix.append(ch)
                else:
                    possible = False
                    break
            
            if not possible:
                continue
                
            # If i == n, it means exact match with target, but we need strictly greater
            if i == n:
                continue
                
            # For position i, choose the smallest character strictly greater than target[i]
            target_ch = target[i]
            available_chars = sorted([ch for ch in prefix_counts if prefix_counts[ch] > 0 and ch > target_ch])
            
            if available_chars:
                next_ch = available_chars[0]
                prefix.append(next_ch)
                prefix_counts[next_ch] -= 1
                
                # Fill the rest with smallest remaining characters in sorted order
                for ch in sorted(prefix_counts.keys()):
                    prefix.extend([ch] * prefix_counts[ch])
                
                return "".join(prefix)
                
        return ""