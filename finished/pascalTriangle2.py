'''
Problem: 119. Pascal's Triangle II
Input: rowIndex - the index number of a row in Pascal Triangle
Output: An array list of integer that represent the kth index row in Pascal Triangle
Explanation:
    Using extra spaces approach, we allocate an temp array start from
    row index 3 of Pascal Triangle ([1,2,1]). We loop starting from
    row index 3 to given rowIndex. Each time we loop, we create new
    temp array with i from 3->rowIndex and traverse through prev
    result to fill up our current temp array. We start filling in
    at index 1 -> n-1. Leaving first and last index with 1. Each
    time we finish filling up array, we add it to the result array
    and continue calculate the next row. When reach the rowIndex
    that we are looking for, stop loop and return the result array.
    Using only k spaces approach, we allocate enough space from
    given rowIndex with 1. We calculate from row index 2 to given
    rowIndex on the same array. To do this, we have 1 loop going
    from left to right and another inner loop from right to left.
    The inner loop will add it current value with the value to the
    left of it [j] + [j-1]. Once the inner loop is done adding, we
    increment the outer loop by 1 and the process starts again. We
    return result array. Run time is O(mn) for m is the length of
    whole array and n is the number of time we add number backward.
    Space complexity is O(rowIndex). For extra space approach, same
    run time but space complexity is O(n).
'''

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        # Using extra space approach
        # res = [1,2,1]
        #
        # for i in range(3, rowIndex+1):
        #     temp = [1] * (i + 1)
        #     for j in range(len(res)-1):
        #         temp[j + 1] = res[j] + res[j+1]
        #     res = temp
        # print(res)

        # Using k number of space
        res = [1] * (rowIndex+1)

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                res[j] = res[j] + res[j-1]
        print(res)

sol = Solution()
sol.getRow(2)
sol.getRow(3)
sol.getRow(4)
sol.getRow(10)
