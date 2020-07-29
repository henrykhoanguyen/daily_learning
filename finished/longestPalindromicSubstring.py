class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return s
        res = ""

        def isPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # print(s[left + 1 : right])
            return s[left + 1 : right]

        for i in range(len(s)):
            # Check even cases
            even = isPalindrome(i, i+1)
            odd = isPalindrome(i-1, i+1)
            res = max(even, odd, res, key=len)

        print(res)
        return res

sol = Solution()
sol.longestPalindrome("babad")