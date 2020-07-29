from typing import List
# import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tlen = len(tickets)
        dic = {}
        res = []
        src = "JFK"
        stack = []
        # tickets.sort()

        # This iteration takes O(n) time to traverse
        # thru tickets list to construct dictionary
        for i in range(tlen):
            if tickets[i][0] not in dic:
                dic[tickets[i][0]] = [tickets[i][1]]
            else:
                # heapq.heappush(dic[tickets[i][0]],tickets[i][1])
                dic[tickets[i][0]].append(tickets[i][1])

        for i in dic.keys():
            dic[i].sort(reverse=True)

        # print(dic)
        stack.append(src)

        # another O(n) time to traverse thru dictionary
        while len(stack) > 0: #src in dic and len(dic[src]) > 0:
            # print(dic[src][0])
            src = stack[-1]

            if src in dic and len(dic[src]) > 0:
                stack.append(dic[src].pop())
                # if len(dic[src]) > 0:
                #     del dic[src][0]
                # else:
                #     del dic[src]
            else:
                res.append(stack.pop())

        print(res[::-1])

sol = Solution()
sol.findItinerary( [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]] )
sol.findItinerary( [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] )
sol.findItinerary( [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] )
sol.findItinerary(
[["EZE","TIA"],["EZE","AXA"],["AUA","EZE"],["EZE","JFK"],["JFK","ANU"],["JFK","ANU"],["AXA","TIA"],["JFK","AUA"],["TIA","JFK"],["ANU","EZE"],["ANU","EZE"],["TIA","AUA"]]
)