'''
Problem: 171. Excel Sheet Column Number
Input: s: str -> a string of uppercase char from A - Z
Output: a number of column number combined A - 1; Z - 26; AA - 27
Explanation:
    We traverse through give string s to get ascii value
    of each char. We subtract it to A to get its position
    in the alphabet as digit. The math would be as followed
    res = res * 26 + digit.
    For example: "AB" = (1*26*26) + (2*26)
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return 0

        res = 0

        for char in s:
            digit = ord(char) - ord("A") + 1
            res = res * 26 + digit
        print(res)
        return res

sol = Solution()
sol.titleToNumber("ZY")
sol.titleToNumber("AB")