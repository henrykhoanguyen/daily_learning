
class Solution:
    def candyCrush(self, s: str) -> str:
        if len(s) <= 0:
            return s

        stack = []
        count = 1
        slen = len(s)
        stack.append(s[0])
        for i in range(1, slen):
            if s[i] == stack[-1] and count != 3:
                count += 1
                stack.append(s[i])
            elif s[i] == stack[-1] and count == 3:
                while count > 0:
                    stack.pop(-1)
                    count -= 1
            else:
                count = 1
                stack.append(s[i])
        print(stack)

sol = Solution()
sol.candyCrush("aaabbbc")
sol.candyCrush("aabbbacd")
sol.candyCrush("aabbccddeeedcba")
sol.candyCrush("aaabbbacd")