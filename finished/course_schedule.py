from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return False
        visited = []
        visit = []
        dic = defaultdict(list)

        for i in prerequisites:
            dic[i[0]].append(i[1])
        print(dic)

        visit.append(prerequisites[0][0])

        # while visit:
        #     tmp = visit.pop()
        #     if visited:
        #         visited.append(tmp)
        #     else:
        #         return False
        #     for i in dic[tmp]:
        #         visit.append(i)
        return True


sol = Solution()
sol.canFinish(2, [[1,0]])
sol.canFinish(2, [[1,0],[0,1]])