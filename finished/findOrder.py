from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites and numCourses < 1:
            return []
        if not prerequisites and numCourses == 1:
            return [0]

        plen = len(prerequisites)
        adjList = defaultdict(list)
        visited = [0] * numCourses
        stack = []

        # Making adj list
        for dest, src in prerequisites:
            adjList[src].append(dest)

        for i in range(numCourses):
            if not self.dfs(visited, i, stack, adjList):
                print([])
                return []

        print(stack[::-1])

    def dfs(self, visited, loc, stack, adjList):
        if visited[loc] == -1:    # Cycle detected
            return False
        if visited[loc] == 1:     # DAG
            return True

        visited[loc] = -1     # mark as visited

        if loc in adjList:
            for i in adjList[loc]:
                if not self.dfs(visited, i, stack, adjList):
                    return False
        visited[loc] = 1    # mark as finished

        stack.append(loc)
        return True



sol = Solution()
sol.findOrder(2, [[1,0]])
sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
sol.findOrder(2, [[0,1],[1,0]])