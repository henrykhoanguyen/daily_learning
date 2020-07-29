from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj = defaultdict(list)

        for start, dest,cost in flights:
            adj[start].append((dest, cost))

        queue = []
        queue.append((0, src, K+1))

        while len(queue) > 0:
            dest, vertex, e = heapq.heappop(queue)

            if vertex == dst:
                print(dest)
                return dest
            if e > 0:
                for i in adj[vertex]:
                    heapq.heappush(queue, (dest + i[1], i[0], e - 1))
        return -1

sol = Solution()
sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)