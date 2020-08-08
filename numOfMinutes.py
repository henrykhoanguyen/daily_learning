'''
Problem: 1376. Time Needed to Inform All Employees
Input:
Output:
Explanation:

'''

from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # build an adj list of who is manager of whom
        # and traverse through list using dfs to calculate time needed
        if n == 1:
            return informTime[0]

        mlen = len(manager)
        ilen = len(informTime)



        return 0


sol = Solution()
sol.numOfMinutes(1, 0, [-1], [0])
sol.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0])
sol.numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1])
sol.numOfMinutes(15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
sol.numOfMinutes(4, 2, [3,3,-1,2], [0,0,162,914])