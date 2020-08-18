'''
Problem: 1376. Time Needed to Inform All Employees
Input:
    headID - ID of top manager
    manager - an integer array of manager ID
            with index as their respective employee
    informTime - an integer array of time people need
            to make to inform someone. index is that
            employee ID
    n - number of employee
Output: total time it takes to inform all employee
Explanation:

'''

from typing import List
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # build an adj list of who is manager of whom
        # and traverse through list using dfs to calculate time needed
        if n == 1:
            return informTime[0]

        mlen = len(manager)
        ilen = len(informTime)

        adj_list = defaultdict(list)
        self.res = 0

        for i in range(mlen):
            if manager[i] != -1:
                if manager[i] not in adj_list:
                    adj_list[manager[i]] = [i]
                else:
                    adj_list[manager[i]].append(i)


        print(adj_list)

        def calcInformTime(id, time):
            self.res = max(self.res, time)

            for i in adj_list[id]:
                calcInformTime(i, time + informTime[id])

        calcInformTime(headID, 0)

        print(self.res)
        return self.res


sol = Solution()
sol.numOfMinutes(1, 0, [-1], [0])
sol.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0])
sol.numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1])
sol.numOfMinutes(15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
sol.numOfMinutes(4, 2, [3,3,-1,2], [0,0,162,914])