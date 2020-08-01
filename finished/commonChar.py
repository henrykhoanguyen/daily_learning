'''
Problem: 1002. Find Common Characters
Input: A - a list array of string
Output: a list array of string/char that are common
        amount all given input strings.
Explanation:
    We use collections.Counter to quickly count
    number of appearance of each letter in a word
    After, we compare counter of each word to each
    other and update the counter again with the
    minimum appearance of that letter across all
    word in given list array string. Then, we add
    each letter into result array if their counter
    is larger than 0. a letter can appear more than
    1 in result array if its counter is larger than 1
'''

from typing import List
from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []

        toCompare = Counter(A[0])         # count number of appearance of each letter of first word
        alen = len(A)                     # length of array string A
        res = []                          # declare result array

        # compare each word to the first word and count
        # the smallest number of appearance of each letter.
        for i in range(1, alen):
            tmp = Counter(A[i])
            for letter, count in toCompare.items():
                toCompare[letter] = min(count, tmp[letter])

        # add any letter with appearance more than 0 to
        # result array.
        for letter, count in toCompare.items():
            if count > 0:
                res += [letter] * count
        print(res)
        return res

sol = Solution()
sol.commonChars(["bella", "label", "roller"])
sol.commonChars(["cool", "lock", "cook"])