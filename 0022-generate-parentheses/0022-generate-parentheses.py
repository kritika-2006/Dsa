class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Base Case: Valid combination reached
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Choice 1: Add an open parenthesis if count < n
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Choice 2: Add a close parenthesis if close_count < open_count
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return result