class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                temp = []
                # Pop characters until the matching opening parenthesis is found
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the opening parenthesis '('
                if stack and stack[-1] == '(':
                    stack.pop()
                # Push the reversed characters back onto the stack
                stack.extend(temp)
            else:
                stack.append(char)
                
        return "".join(stack)