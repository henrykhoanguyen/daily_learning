from typing import List
import itertools

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        if not A:
            return ""

        # Get all possible permutation from list array A
        times = itertools.permutations(sorted(A, reverse=True))

        # validate each index to ensure that times is correct
        for time in times:
            if time[:2] < (2,4) and time[2] < 6:
                print("%d%d:%d%d" % time)
                return "%d%d:%d%d" % time
        print("u gey")
        return "u gey"

sol = Solution()
sol.largestTimeFromDigits([1,2,3,4])
sol.largestTimeFromDigits([5,5,5,5])
