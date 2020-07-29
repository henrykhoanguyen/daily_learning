from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        lst = sorted(people, key=lambda x: (-x[0], x[1]))
        out = []
        for x in lst:
            out.insert(x[1], x)
        print(out)
        # people = sorted(people)
        # plen = len(people)
        # res = [None] * plen
        # count = 0
        #
        # for i in range(plen):
        #     count = people[i][1]
        #     for j in range(plen):
        #         if res[j] is None and count == 0:
        #             res[j] = people[i]
        #             break
        #         elif res[j] is None or res[j][0] >= people[i][0]:
        #             count -= 1
        # return res
        # print(res)

sol = Solution()
sol.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])