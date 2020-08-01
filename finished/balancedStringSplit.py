'''
Problem: 1221. Split a String in Balanced Strings
Input: string s with only 2 letter
Output: number of ways to split string
Explanation:
    Greedy Approach - using a counter to keep count of
    R and L. if char is R, we add 1 to counter, and -1
    if char is L. if counter == 0, then we add 1 to
    result counter to denote that a string with equal
    amount of R and L is found. return that result
    counter. Run time is O(n).

    Stack Approach - similar to Greedy Approach but we
    use stack to keep count of R and L. we add to stack
    if current char in string is the same as the char at
    top of the stack. We pop if it's different. If stack
    is empty, we increment result counter by 1. Return
    result counter. Run time is O(n).
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s:
            return 0

        slen = len(s)
        counter = 0
        res = 0

        # Stack Approach
        # stack = []
        #
        # stack.append(s[0])
        #
        # for i in range(1, slen):
        #     if stack and stack[-1] != s[i]:
        #         stack.pop()
        #     else:
        #         stack.append(s[i])
        #
        #     if not stack:
        #         counter += 1

        # Greedy Approach
        for i in range(slen):
            if s[i] == "R":
                counter += 1
            elif s[i] == "L":
                counter -= 1

            if counter == 0:
                res += 1
        print(res)

sol = Solution()
sol.balancedStringSplit("RLRRLLRLRL")
sol.balancedStringSplit("RLLLLRRRLR")
sol.balancedStringSplit("LLLLRRRR")
sol.balancedStringSplit("RLRRRLLRLL")
