'''
Problem: 967. Numbers With Same Consecutive Differences
Input:
    N: int -> number of digit per number
    K: int -> the differences between consecutive digits
Output:
    res: List[int] -> return a list of numbers with same consecutive differences
Explanation:
    This is a dynamic programming problem. We use DFS to calculate the next
    possible digit that can be added into our number. Such digit has to be
    the result of the difference or sum of K. There are two base case:
    N == 1 and K == 0. When N == 1, we return digit range from 0 to 10. When
    K == 0, we return a number with N length with every digit's difference
    is 0. As we go through our DFS, we find a new digit and check if it is
    bigger than 0 and smaller than 9; otherwise we won't add it our current
    number. Once our current number's length == N, we add it to our result
    array. Return result array once all possibilities are explored. Run time
    of this program is O(2^N)
'''


from typing import List

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        res = []
        if N == 1:
            print([i for i in range(10)])
            return [i for i in range(10)]

        if K == 0:
            print([int(''.join(str(_) * N)) for _ in range(1, 10)])
            return [int(''.join(str(_) * N)) for _ in range(1, 10)]

        def dfs(num, tmp):
            if num > 9 or num < 0:
                return

            if len(str(int(tmp))) == N:
                # print(tmp)
                res.append(int(tmp))
                return

            dfs(num + K, tmp + str(num + K))
            dfs(num - K, tmp + str(num - K))

        for i in range(1, 10):
            dfs(i, str(i))
        print(res)
        return res


sol = Solution()
sol.numsSameConsecDiff(2, 1)
sol.numsSameConsecDiff(3, 7)
sol.numsSameConsecDiff(3, 2)
sol.numsSameConsecDiff(1, 0)
sol.numsSameConsecDiff(3, 0)