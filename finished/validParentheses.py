class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if len(s) < 1:
            return True
        stack = []
        dic = {")": "(", "}": "{", "]": "["}
        slen = len(s)

        for i in range(slen):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if stack and stack[-1] == dic[s[i]]:
                    stack.pop(len(stack) - 1)
                else:
                    return False
        if stack:
            return False
        return True

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
print(sol.isValid("){"))
print(sol.isValid("(("))
print(sol.isValid("))"))