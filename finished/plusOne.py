from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dlen = len(digits)
        # carrier = 0
        #
        # if digits[-1] + 1 > 9:
        #     carrier += 1
        #     digits[-1] = 0
        # else:
        #     digits[-1] += 1
        #     print(digits)
        #     return digits
        #
        # for i in range(dlen-2, -1, -1):
        #     if digits[i] + carrier <= 9:
        #         digits[i] += carrier
        #         carrier = 0
        #     else:
        #         digits[i] = (digits[i] + carrier) % 10
        #         carrier = 1
        #
        # if carrier == 1:
        #     digits.insert(0, carrier)

        for i in range(dlen-1, -1, -1):
            if digits[i] + 1 > 9:
                digits[i] = 0
            else:
                digits[i] += 1
                print(digits)
                return digits

        digits.insert(0, 1)
        print(digits)

sol = Solution()
sol.plusOne([1,2,3])
sol.plusOne([4,3,2,2,1])
sol.plusOne([9])
sol.plusOne([8,9])
sol.plusOne([9,9])