class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) <= 1:
            return s

        s = s.split()
        right = len(s) - 1
        left = 0

        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1

        print(" ".join(s))

        # for i in range(slen-1, -1, -1):
        #     if s[i] != "":
        #         res += s[i] + " "


sol = Solution()
sol.reverseWords("the sky is blue")
sol.reverseWords("  hello world!  ")
sol.reverseWords("a good   example")