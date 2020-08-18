'''
Problem: 1103. Distribute Candies to People
Input:
    candies: int -> number of candies to be distributed
    num_people: int -> number of people to distribute
Output:
    result: List(int) -> a result array of after all
            candies are distributed
Explanation:
    This is a math problem. We need to calculate number of
    candies to give to each person each loop. The math for
    it would be candy = loop*num_people + (index+1). The
    loop * num_people denotes the iteration we are currently
    on. This helps us decide how many candies to give to
    each person. We also need to consider that current candy
    with the number of candies left over by finding the min
    of both of them. Run time for this problem is O(n) for
    n is the number of candies in worst case scenarios.
'''

from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        if not candies or not num_people:
            return []

        counter, loop = 0, 0

        res = [0] * num_people

        while candies > 0:

            if counter == num_people:
                loop += 1
                counter = 0

            curr_candy = loop * num_people + (counter + 1)

            res[counter] += min(curr_candy, candies)

            candies -= curr_candy
            counter += 1

        print(res)

sol = Solution()
sol.distributeCandies(7, 4)
sol.distributeCandies(10, 3)
