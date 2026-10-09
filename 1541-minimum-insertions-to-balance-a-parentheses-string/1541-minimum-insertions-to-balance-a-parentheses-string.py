class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_close = 0  # Number of ')' needed
        
        for char in s:
            if char == '(':
                # If we need an odd number of ')', it means we had a single ')' 
                # waiting for its partner before this new '(' arrived.
                if needed_close % 2 != 0:
                    insertions += 1      # Insert 1 ')' to complete the pair
                    needed_close -= 1    # Balance the single ')'
                
                needed_close += 2        # Each '(' requires two ')'
                
            else:  # char == ')'
                needed_close -= 1
                
                # We have an extra ')' without an open '('
                if needed_close < 0:
                    insertions += 1      # Insert 1 '('
                    needed_close += 2    # The inserted '(' expects 2 ')', 1 is matched now
                    
        return insertions + needed_close