'''
Problem: 904. Fruit Into Baskets
Input:
    tree: List[int] -> a row of different kind of tree
Output:
    res: int -> the largest number of fruits picking
            from 2 kinds of tree consecutive.
Explanation:
    We have 2 pointers to traverse through tree array; right one
    will keep track of new tree and record it in a hash table and
    a left pointer that help removing tree. First, we have right
    ptr add new tree into hash table and need counting number of
    occurrence. Once our hash table's length reaches 3, we move
    our left ptr to the right until the length of hash table is
    less than or equal to 2. As we move our left ptr, we remove
    decrement tree count from hash table and remove it entirely
    if it reaches 0. Once our hash table length is 2, we continue
    increment right pointer. This ensures that there will only be
    2 kinds of fruit at all time. Every iteration, we update our
    result variable with the largest consecutive sub array that
    give us the most fruit. Run time complexity of this algorithm
    is O(n) time.
'''

from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0

        tlen = len(tree)
        left = 0
        dic = {}
        res = 0

        for right in range(tlen):
            if tree[right] not in dic:
                dic[tree[right]] = 1
                while len(dic) > 2:
                    dic[tree[left]] -= 1
                    if not dic[tree[left]]:
                        del dic[tree[left]]
                    left += 1
            else:
                dic[tree[right]] += 1
            res = max(res, right - left + 1)
        print(res)


sol = Solution()
sol.totalFruit([1,2,1])
sol.totalFruit([0,1,2,2])
sol.totalFruit([1,2,3,2,2])
sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4])