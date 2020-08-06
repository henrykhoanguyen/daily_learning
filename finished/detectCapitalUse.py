'''
Problem: 520. Detect Capital
Input: word: str - a word with randomized capitalization
Output: boolean value if a word follow capitalization rule
Explanation:
    We use a counter to count number of capitalized letter
    in a word. If the number is equal to the length of
    word, then it's capitalized correctly. If only the
    first letter is capitalized, then it's capitalized
    correctly. If none is capitalized, then it's
    capitalized correctly. Otherwise, it's not capitalized
    correctly. Run time is O(n) time.
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True

        wlen = len(word)
        capital = 0

        if wlen == 1 and word[0].isupper():
            return True

        for i in range(wlen):
            if word[i].isupper():
                capital += 1

        if capital == wlen or capital == 0:
            return True
        if capital != 1 and capital < wlen:
            return False
        if capital == 1 and word[0].isupper():
            return True
        return False

sol = Solution()
print(sol.detectCapitalUse("USA"))
print(sol.detectCapitalUse("FlaG"))
print(sol.detectCapitalUse("Hello"))
print(sol.detectCapitalUse("nice"))
print(sol.detectCapitalUse("msdfK"))