'''
Problem: 987. Vertical Order Traversal of a Binary Tree
Input: TreeNode -> a binary tree
Output: a result list in vertical order traversal
Explanation:
    Using a hashtable to store location of each node.
    We also use: col and row to keep track of each
    node's positions in result array. Using col as
    hash key and to notice which specific index a
    node will be stored in inside the result array
    and using row to notice which node go before each
    other when there are more than 1 node in a
    specific index in result array. To traverse thru
    Binary Tree, we use DFS. We add node to hashtable
    with its row value, then traverse to its child
    nodes. Each time we traverse to left child node,
    col - 1; and to right child node, col + 1. This
    will assign each node with its column value, so
    that it can be used as key in hashtable. Run time
    complexity is O(V + (R * C)) for V - vertices or
    nodes, R - rows, and C - columns.
'''
from typing import List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        self.cache = defaultdict(list)
        self.maxCol, self.minCol = 0,0
        self.dfs(root, 0, 0)    # node, row, col
        res = []
        # print(self.cache)
        index = 0
        for i in range(self.minCol, self.maxCol + 1):
            res.append([])
            for j in sorted(self.cache[i]):
                res[index].append(j[1])
            index += 1
        print(res)
        return res

    def dfs(self, node, row, col):
        if not node:
            return

        self.cache[col].append((row, node.val))
        self.minCol = min(self.minCol, col)
        self.maxCol = max(self.maxCol, col)
        if node.left:
            self.dfs(node.left, row + 1, col - 1)
        if node.right:
            self.dfs(node.right, row + 1, col + 1)

        return


sol = Solution()
# [3,9,20,null,null,15,7]
sol.verticalTraversal(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))

# [1,2,3,4,5,6,7]
sol.verticalTraversal(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))))

# [0,8,1,null,null,3,2,null,4,5,null,null,7,6]
sol.verticalTraversal(TreeNode(0, TreeNode(8), TreeNode(1, TreeNode(3, None, TreeNode(4, None, TreeNode(7))), TreeNode(2, TreeNode(5, TreeNode(6))))))
