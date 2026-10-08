class Solution:

    def removeOuterParentheses(self, s: str) -> str:
        res = []
        open_count = 0

        for c in s:
            if c == "(":
                if open_count > 0:
                    res.append(c)
                open_count += 1
            else:
                open_count -= 1
                if open_count > 0:
                    res.append(c)

        return "".join(res)