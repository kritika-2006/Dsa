class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find the first and last occurrence of each character
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
            
        intervals = []
        
        # Step 2: Create valid intervals for each unique character
        for c in set(s):
            l, r = first[c], last[c]
            valid = True
            i = l
            while i <= r:
                # If a character inside our window appears before our start, it's invalid
                if first[s[i]] < l:
                    valid = False
                    break
                # Expand the right bound if the current character's last occurrence is further
                r = max(r, last[s[i]])
                i += 1
                
            if valid:
                intervals.append((l, r))
        
        # Step 3: Greedy interval scheduling - sort by end index
        intervals.sort(key=lambda x: x[1])
        
        res = []
        last_end = -1
        
        # Step 4: Pick non-overlapping intervals
        for l, r in intervals:
            if l > last_end:
                res.append(s[l:r+1])
                last_end = r
                
        return res