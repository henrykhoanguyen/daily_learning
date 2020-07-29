# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        temp = left
        root.left = right
        root.right = temp

        return root
sol = Solution()
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
root = sol.invertTree(root)
print(root)