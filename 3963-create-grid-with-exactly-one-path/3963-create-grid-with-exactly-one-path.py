class Solution:
    def constructGrid(self, m: int, n: int) -> list[str]:
        grid = []
        # First row is entirely free '.'
        grid.append("." * n)
        
        # All subsequent rows are obstacles '#' except the last column '.'
        for i in range(1, m):
            grid.append("#" * (n - 1) + ".")
            
        return grid

    # Aliases for safety
    createGrid = constructGrid
    solve = constructGrid