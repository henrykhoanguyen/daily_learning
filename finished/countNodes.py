# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.counter = 0

        def dfs(root):
            if root == None:
                return
            self.counter += 1
            dfs(root.right)
            dfs(root.left)
        dfs(root)
        print(self.counter)

sol = Solution()
sol.countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6))))
