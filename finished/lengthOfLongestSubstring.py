class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        slen = len(s)
        unq = set()
        res = 0

        while l < slen and r < slen:
            if s[r] not in unq:
                unq.add(s[r])
                r += 1
                # res = max(res, r - l)
            else:
                unq.remove(s[l])
                l += 1
            res = max(res, r - l)

        print(res)


sol = Solution()
sol.lengthOfLongestSubstring("abcabcbb")
sol.lengthOfLongestSubstring("bbbbb")
sol.lengthOfLongestSubstring("pwwkew")
sol.lengthOfLongestSubstring(" ")