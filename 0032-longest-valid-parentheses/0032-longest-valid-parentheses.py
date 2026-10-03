class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base index for length calculation
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Current ')' is unmatched; set it as the new base boundary
                    stack.append(i)
                else:
                    # Valid substring length = current_index - top_of_stack_index
                    max_length = max(max_length, i - stack[-1])
                    
        return max_length