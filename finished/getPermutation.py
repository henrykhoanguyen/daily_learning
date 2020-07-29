import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factor = [1] * n
        num = []
        res = ""

        # get factorial list
        for i in range(1, n):
            factor[i] = factor[i - 1] * (i+1)
        # print(factor)

        # get list of indices
        for i in range(1, n+1):
            num.append(i)
        # print(num)
        k -= 1

        for i in range(n, 0, -1):
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(num[index])
            num.remove(num[index])
            # print(num, index)
        print(res)


sol = Solution()
sol.getPermutation(3,3)
sol.getPermutation(3,2)
sol.getPermutation(4,9)
sol.getPermutation(5,12)