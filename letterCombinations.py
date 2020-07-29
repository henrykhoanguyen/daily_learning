from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []

        phone = {
            "2": ["a","b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["q", "p", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        dlen = len(digits)
        res = []

        for d in digits:


sol = Solution()
sol.letterCombinations("23")
sol.letterCombinations("19")
sol.letterCombinations("10")
sol.letterCombinations("345")