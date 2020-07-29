class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourAngle = (hour + (minutes/60)) * 30
        minuteAngle = minutes * 6

        angle = abs(hourAngle - minuteAngle)

        print(min(angle, 360 - angle))


sol = Solution()
sol.angleClock(12, 30)
sol.angleClock(3, 30)
sol.angleClock(3, 15)
sol.angleClock(4, 50)
sol.angleClock(12, 0)