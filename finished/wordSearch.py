from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False

        rlen = len(board)
        clen = len(board[0])
        tmp = word
        for r in range(rlen):
            for c in range(clen):
                if board[r][c] == word[0]:
                    if self.dfs(board,r,c, tmp):
                        print(True)
                        return True
        print(False)
        return False

    def dfs(self, board, r, c, word):
        if len(word) < 1:
            return True

        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == "#":
            return False

        if board[r][c] != word[0]:
            return False

        tmp = board[r][c]

        board[r][c] = "#"

        found = self.dfs(board, r + 1, c, word[1:]) or self.dfs(board, r - 1, c, word[1:]) or self.dfs(board, r, c + 1, word[1:]) or self.dfs(board, r, c - 1, word[1:])

        board[r][c] = tmp
        return found

sol = Solution()
sol.exist(
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ],
    "ABCCED"
)

sol.exist(
    [
      ['A']
    ],
    "A"
)

sol.exist(
    [
        [""]
    ],
    "A"
)

sol.exist(
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCB"
)