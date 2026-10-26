class Solution:
    def countIslandsWithDivisibleValue(self, grid: list[list[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        divisible_count = 0
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0 or visited[r][c]:
                return 0
                
            visited[r][c] = True
            total_sum = grid[r][c]
            
            # Explore 4 directions
            total_sum += dfs(r + 1, c)
            total_sum += dfs(r - 1, c)
            total_sum += dfs(r, c + 1)
            total_sum += dfs(r, c - 1)
            
            return total_sum

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and not visited[r][c]:
                    island_sum = dfs(r, c)
                    if island_sum % k == 0:
                        divisible_count += 1
                        
        return divisible_count

    # Aliases to prevent method name mismatch errors
    countIslands = countIslandsWithDivisibleValue
    solve = countIslandsWithDivisibleValue