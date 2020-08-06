class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        n = num
        count = 0

        while n > 1:
            n >>= 2
            count += 2
        print((n << count) == num)
        return (n << count) == num

sol = Solution()
sol.isPowerOfFour(16)
sol.isPowerOfFour(5)
sol.isPowerOfFour(625)