class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        
        # Collect all coordinates of 1s in both images
        pts1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        pts2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count the frequency of each translation vector (r2 - r1, c2 - c1)
        from collections import Counter
        vector_counts = Counter()
        
        for r1, c1 in pts1:
            for r2, c2 in pts2:
                vector_counts[(r2 - r1, c2 - c1)] += 1
                
        # Return the maximum overlap count for any translation vector (or 0 if no 1s overlap)
        return max(vector_counts.values()) if vector_counts else 0