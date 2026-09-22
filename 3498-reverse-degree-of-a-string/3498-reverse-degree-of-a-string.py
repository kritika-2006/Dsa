class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        for i, char in enumerate(s, 1):
            # Position in reversed alphabet: 'a' is 26, 'b' is 25, ..., 'z' is 1
            rev_pos = 26 - (ord(char) - ord('a'))
            total_degree += rev_pos * i
        return total_degree