from typing import List
import collections

class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isWord = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):
        node = self.root
        for w in words:
            node = node.child[w]
        node.isWord = True

    def search(self, words):
        node = self.root
        for w in words:
            node = node.child.get(w)
            if not node:
                return False
        return node.isWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = TrieTree()
        node = trie.root

        rlen = len(board)
        clen = len(board[0])

        for w in words:
            trie.insert(w)

        for r in range(rlen):
            for c in range(clen):
                self.dfs(board, node, r, c, "", res)
        print(res)

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        tmp = board[i][j]
        node = node.child.get(tmp)
        if not node:
            return
        board[i][j] = "#"

        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        board[i][j] = tmp

sol = Solution()
sol.findWords(
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"]
)