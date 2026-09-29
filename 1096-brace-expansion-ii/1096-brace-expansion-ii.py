class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def helper(s):
            stack = [[]]
            op = '+'
            i = 0
            while i < len(s):
                if s[i] == '{':
                    bal = 1
                    j = i + 1
                    while j < len(s) and bal > 0:
                        if s[j] == '{': bal += 1
                        elif s[j] == '}': bal -= 1
                        j += 1
                    sub = helper(s[i+1:j-1])
                    if op == '*':
                        stack[-1] = [x + y for x in stack[-1] for y in sub]
                    else:
                        stack.append(sub)
                        op = '*'
                    i = j
                elif s[i] == ',':
                    op = '+'
                    i += 1
                else:
                    j = i
                    while j < len(s) and s[j].isalpha():
                        j += 1
                    word = s[i:j]
                    if op == '*':
                        stack[-1] = [x + word for x in stack[-1]]
                    else:
                        stack.append([word])
                        op = '*'
                    i = j
            return sorted(list(set(sum(stack, []))))
        
        return helper(expression)