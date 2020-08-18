'''
Problem: 482. License Key Formatting
Input:
    S: str -> a string to be format,
    K: int -> a formatting rule
Output:
    res: str -> a formatted result string
Explanation:
    We remove all dashes in string and join them together.
    Then we traverse from left to right of string and add
    each char to result string until we reach K number of
    char, then insert a dash in front of it. Return result
    string. Run time complexity is O(n) time for n is the
    length of the string. This is traversing backwards
    approach. A forwards approach, we would need to
    calculate for the header of string since it can be at
    any length lesser than K. To calculate for header,
    head = len(str) % K. We then insert str[:head] into
    result string first. Then traverse through string in
    Kth step to get Kth number of substring to append into
    result string. Run time of this approach is O(n/K)
'''

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        if not S:
            return ""

        res = ""
        S = "".join(S.upper().split("-"))
        k = K
        for i in range(len(S)-1, -1, -1):
            res = S[i] + res
            k -= 1
            if k == 0 and i != 0:
                res = "-" + res
                k = K
        print(res)
        return res

sol = Solution()
sol.licenseKeyFormatting("5F3Z-2e-9-w", 4)
sol.licenseKeyFormatting("2-5g-3-J", 2)
sol.licenseKeyFormatting("2-5gA0-3s-J", 3)