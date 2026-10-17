class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Helper function to calculate sum of digits of a number
        def get_digit_sum(x: int) -> int:
            return sum(int(digit) for digit in str(x))
        
        # Step 1: Pair each element with its original index
        # (val, original_index)
        arr = [(val, i) for i, val in enumerate(nums)]
        
        # Step 2: Sort based on custom criteria:
        # Primary key: digit sum
        # Secondary key: actual value
        arr.sort(key=lambda x: (get_digit_sum(x[0]), x[0]))
        
        # Step 3: Find minimum swaps using cycle decomposition
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or element is already at its correct target position
            if visited[i] or arr[i][1] == i:
                continue
            
            # Find the length of the cycle
            cycle_size = 0
            curr = i
            
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][1]
                cycle_size += 1
                
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps