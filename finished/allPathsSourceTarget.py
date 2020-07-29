from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return graph

        glen = len(graph)
        res = []


'''
        adj = {src: des for src, des in enumerate(graph)}

        for node in adj[0]:
            path = [0, node]
            self.helper(path, node, adj, res)

        print("res:", res)
        return res

    def helper(self, path, node, adj, res):

        if not adj[node]:
            res.append(path)
            return

        for i in adj[node]:
            self.helper(path + [i], i, adj, res)
        return
'''

sol = Solution()
sol.allPathsSourceTarget([[1,2], [3], [3], []])
sol.allPathsSourceTarget([[1,2,3], [4,5], [4], [5], [], []])