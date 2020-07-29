class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 and not num2:
            print("")
            return ""
        if not num1:
            print(num2)
            return num2
        if not num2:
            print(num1)
            return num1

        len1, len2 = len(num1), len(num2)
        carry = 0
        res = []
        while len1 > 0 or len2 > 0 or carry != 0:
            num = 0

            if len1 > 0:
                num += int(num1[len1 - 1])

            if len2 > 0:
                num += int(num2[len2 - 1])

            if carry != 0:
                num += carry

            res.append(str(num % 10))
            carry = num // 10

            len1 -= 1
            len2 -= 1

        print("".join(res[::-1]))


sol = Solution()
sol.addStrings("9", "99")
sol.addStrings("1", "2")
sol.addStrings("90", "12")
sol.addStrings("", "2")
sol.addStrings("2", "")
sol.addStrings("", "")
sol.addStrings("99", "1")