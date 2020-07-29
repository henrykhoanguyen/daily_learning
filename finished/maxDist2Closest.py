from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if not seats:
            return 0
        maxDist = 0
        count = 0
        slen = len(seats)

        while seats[maxDist] == 0:
            maxDist += 1

        for i in range(slen):
            if seats[i] == 0:
                count += 1
            else:
                maxDist = max(maxDist, (count+1) // 2)
                count = 0

        print(max(maxDist, count))

sol = Solution()
sol.maxDistToClosest([1,0,0,0,0,1,0,1])
sol.maxDistToClosest([1,0,0,0,0,0])
sol.maxDistToClosest([0,0,0,0,0,1])