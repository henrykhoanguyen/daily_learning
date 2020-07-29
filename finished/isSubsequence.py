class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        rlen = len(t)
        clen = len(s)

        ''' Longest common Subsequence approach '''
        dp = [[0] * (clen+1) for _ in range(rlen+1)]

        for r in range(rlen):
            for c in range(clen):
                if s[c] == t[r]:
                    dp[r+1][c+1] = 1 + dp[r][c]
                else:
                    dp[r + 1][c + 1] = max(dp[r][c+1], dp[r+1][c])
        print("Longest common Subsequence approach", dp[rlen][clen] == clen)

        ''' Queue approach '''

        print("Queue approach")

        ''' Slicing approach '''
        boolean = True
        for c in s:
            index = t.find(c)
            if index != -1:
                t = t[index+1:]
            else:
                boolean = False
                break
        print("Slicing approach", boolean)



sol = Solution()
sol.isSubsequence("abc", "ahbgdc")
sol.isSubsequence("axc", "ahbgdc")