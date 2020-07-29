class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1

        k2, k3, k5 = 0,0,0
        res = [0] * n
        res[0] = 1

        for i in range(1,n):
            res[i] = min(res[k2]*2, res[k3]*3, res[k5]*5)

            if res[i] == res[k2]*2:
                k2 += 1
            if res[i] == res[k3]*3:
                k3 += 1
            if res[i] == res[k5]*5:
                k5 += 1
            # print(k2, k3, k5)

        print(res)


sol = Solution()
sol.nthUglyNumber(10)
sol.nthUglyNumber(11)

