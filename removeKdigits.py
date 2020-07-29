class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if len(num):
            return num





sol = Solution()
sol.removeKdigits("1432219", 3)
sol.removeKdigits("10200", 1)
sol.removeKdigits("10", 2)
sol.removeKdigits("112", 1)
sol.removeKdigits("11111111", 4)