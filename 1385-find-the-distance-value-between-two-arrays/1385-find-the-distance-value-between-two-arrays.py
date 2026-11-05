class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        distance_val = 0
        
        import bisect
        
        for val in arr1:
            # Find the insertion point in sorted arr2 for val - d
            idx = bisect.bisect_left(arr2, val - d)
            
            # Check if the element at idx satisfies the condition |val - arr2[idx]| <= d
            # Or check the element just before idx
            found = False
            if idx < len(arr2) and abs(arr2[idx] - val) <= d:
                found = True
            if idx > 0 and abs(arr2[idx - 1] - val) <= d:
                found = True
                
            if not found:
                distance_val += 1
                
        return distance_val

    # Aliases for platform method name compatibility
    solve = findTheDistanceValue