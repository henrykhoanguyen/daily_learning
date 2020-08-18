'''
Problem: 409. Longest Palindrome
Input: s: string -> a string with random char
Output: int -> the longest possible palindrome generated long string
Explanation:
    Since we can reorder string in such way to make the longest
    possible palindrome, any odd number of char can be made into
    even number of char by minus 1. We all add all even length
    char into result variable. We add odd length char into
    result variable as well after turning it even. If there
    exists an odd length char, we add 1 to result before return
    it. Else return result variable as is. Run time is O(n + m)
    n for the length of string and m for the length of Counter
    after counted all appearance of char.
'''
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        slen = len(s)

        dict = Counter(s)
        res = 0
        odd = 0

        # counting odd numbers and adding it separately
        # maxOdd = 0
        # oddCount = 0
        # # print(dict)
        # for key, val in dict.items():
        #     if val % 2 == 1:
        #         maxOdd = max(maxOdd, val)
        #         oddCount += 1
        #         odd += val
        #     else:
        #         res += val
        #
        # if oddCount != 0:
        #     odd -= (maxOdd + (oddCount - 1))
        # print(maxOdd + res + odd)
        # return (maxOdd + res + odd)

        # adding odd numbers straight into result
        for val in dict.values():
            if val % 2 == 1:
                odd = 1
            res += (val // 2) * 2

        print(res+odd)
        return res + odd

sol = Solution()
sol.longestPalindrome("abccccdd")
sol.longestPalindrome("Aa")
sol.longestPalindrome("abccccb")
sol.longestPalindrome("bb")
sol.longestPalindrome("bba")
sol.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlong"
                      "endureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafin"
                      "alrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproper"
                      "thatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisground"
                      "Thebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetract"
                      "TgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItis"
                      "forusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsono"
                      "blyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonor"
                      "eddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweher"
                      "ehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffr"
                      "eedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")