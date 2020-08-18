'''
Problem: 1286. Iterator for Combination
Input:
    character: str -> a string with sorted char in lexi order
    combinationLength: int -> a required length for each combination.
Output:
    next(): str -> return a string combination
    hasNext(): bool -> return boolean value if there exists a combination
Explanation:

'''

from itertools import permutations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combine = []
        for perm in list(permutations(characters, combinationLength)):
            perm = "".join(sorted(perm))
            if perm not in self.combine:
                self.combine.append(perm)
        print(self.combine)

    def next(self) -> str:
        return self.combine.pop(0)
        # return ""

    def hasNext(self) -> bool:
        if self.combine:
            return True
        return False


iterator = CombinationIterator("abc", 2)
iterator.next()             # returns "ab"
iterator.hasNext()          # returns true
iterator.next()             # returns "ac"
iterator.hasNext()          # returns true
iterator.next()             # returns "bc"
iterator.hasNext()          # returns false