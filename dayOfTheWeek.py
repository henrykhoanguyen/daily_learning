class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1:
            print("")
            return ""

        print("Hello")

sol = Solution()
sol.dayOfTheWeek(31, 8, 2019)