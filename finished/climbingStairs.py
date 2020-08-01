'''
Problem: 70. Climbing Stairs
Input: n: int - number of steps to make to top
Output: number of distinct ways to get to top
Explanation:
    The approach for this problem is dynamic programming.
    The base cases are:
        - to make to 0 step, there is 1 distinct way
        - to make to 1 step, there is 1 distinct way
    Then, to make to 2 steps, there are 2 distinct ways.
    And to make 3 steps, there are 3 distinct ways.
    A pattern we see from this is that i = (i-1) + (i-2)
    distinct ways; meaning to find number of distinct way
    to make 2 steps, we combine number of distinct way to
    make 0 step and 1 step (1 way + 1 way) which equals
    to 2 distinct ways.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1

        res = [1] * (n+1)

        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        print(res[-1])
        return res[-1]

sol = Solution()
sol.climbStairs(2)
sol.climbStairs(3)
sol.climbStairs(4)
sol.climbStairs(5)