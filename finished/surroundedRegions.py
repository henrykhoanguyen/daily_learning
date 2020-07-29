from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rlen = len(board)
        clen = len(board[0])

        for r in range(rlen):
            for c in range(clen):
                if r == 0 or r == (rlen - 1):
                    self.checkAround(r, c, board)
                if c == 0 or c == (clen - 1):
                    self.checkAround(r, c, board)

        for r in range(rlen):
            for c in range(clen):
                if board[r][c] == "1":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

    def checkAround(self, r, c, board):
        if r < 0 or c < 0:
            return
        if r > len(board)-1 or c > len(board[0])-1:
            return
        if board[r][c] == "X" or board[r][c] == "1":
            return

        board[r][c] = "1"

        self.checkAround(r+1, c, board)
        self.checkAround(r-1, c, board)
        self.checkAround(r, c+1, board)
        self.checkAround(r, c-1, board)
        return

sol = Solution()

sol.solve(
    [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
)

sol.solve(
    [
        [ "X", "X", "X", "O", "X", "X"],
        [ "X", "O", "X", "O", "O", "X"],
        [ "X", "X", "O", "X", "X", "O"],
        [ "X", "O", "O", "X", "X", "X"],
        [ "X", "X", "X", "X", "X", "X"]
    ]
)

sol.solve(
    [
        [ "X", "X", "X", "O", "X"],
        [ "X", "X", "O", "X", "O"],
        [ "X", "X", "O", "O", "O"],
        [ "O", "X", "X", "X", "X"],
        [ "X", "X", "O", "O", "X"],
        [ "X", "X", "X", "X", "X"]
    ]
)