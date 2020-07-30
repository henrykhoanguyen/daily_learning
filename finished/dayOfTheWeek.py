'''
Problem: 1185. Day of the Week
Input: day: integer, month: integer, year: integer
Output: day of week - string

Explanation:
    We calculate the number of days from input date
    to 12/31/1970. Then calculate the number of days
    from current date to 12/31/1970. After we find
    the difference between these two number of days.
    We mod it to 7 to get the index of the day inside
    the dayNames array. For dayNames array, index 0
    hold the current day. Run time is O(mn) time.
    m is the  number of days from current date to
    12/31/1970 and n is the number of days from input
    date to 12/31/1970.
'''

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1:
            print("")
            return ""

        # We start 0 at Wed because we know 7/29/2020 is Wednesday
        dayNames = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        knownStart = self.getNumsDay(29, 7, 2020, daysInMonth)
        findDay = self.getNumsDay(day, month, year, daysInMonth)
        # print(knownStart, findDay)
        print(dayNames[(findDay - knownStart) % 7])
        return dayNames[(findDay - knownStart) % 7]

    # Find if year is a leap or not
    def hasLeapDay(self, year):
        return 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0

    # Get number of day since 12/31/1970
    def getNumsDay(self, day, month, year, daysInMonth):
        numsDay = 0

        for i in range(year - 1, 1970, -1):
            numsDay += 365 + self.hasLeapDay(i)

        numsDay += sum(daysInMonth[:month-1])
        numsDay += day

        if month > 2:
            numsDay += self.hasLeapDay(year)
        return numsDay


sol = Solution()
sol.dayOfTheWeek(31, 8, 2019)
sol.dayOfTheWeek(18, 7, 1999)
sol.dayOfTheWeek(15, 8, 1993)
sol.dayOfTheWeek(23, 7, 2025)