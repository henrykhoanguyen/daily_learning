'''
Problem: 763. Partition Labels
Input: S - string
Output: a list of array integer of length of each partition
Explanation:
    First loop will determine the index of the last occurrence
    of each char. This will help us calculate the length of
    each partition. We use left and right variables to keep
    track of the increasing length of partition. Once right
    pointer == current index of character, we know we find the
    longest partition. Then, (right - left + 1) to get the
    length of that partition and append it to result array.
    Run time is O(n) for n is length of string. Space is
    O(26) or O(1).
'''
from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []

        res = []
        lastChar = {ch: i for i, ch in enumerate(S)}
        left, right = 0, 0

        for index, char in enumerate(S):
            right = max(right, lastChar[char])
            if index == right:
                res.append(right - left + 1)
                left = right + 1
        print(res)
        return res


sol = Solution()
sol.partitionLabels("ababcbacadefegdehijhklij")