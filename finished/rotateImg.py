from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rlen = len(matrix)
        clen = len(matrix[0])

        for r in range(rlen//2):
            for c in range(r, clen-r-1):
                temp = matrix[r][c]
                matrix[r][c] = matrix[rlen - 1 - r][c]
                matrix[rlen - 1 - r][c] = matrix[rlen - 1 - r][clen - 1 - c]
                matrix[rlen - 1 - r][clen - 1 - c] = matrix[r][clen - 1 - c]
                matrix[r][clen - 1 - c] = temp

        print(matrix)


sol = Solution()
sol.rotate(
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
)

sol.rotate(
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ]
)