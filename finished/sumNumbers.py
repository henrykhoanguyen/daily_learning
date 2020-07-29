# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        nums = []
        num = ""
        res = 0
        def dfs(root, num):
            if not root:
                return

            num += str(root.val)
            if root.left is not None or root.right is not None:
                dfs(root.left, num)
                dfs(root.right, num)
            else:
                nums.append(num)

        dfs(root, num)
        for i in nums:
            res += int(i)

        print(res)


sol = Solution()
sol.sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0)))
sol.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3)))
sol.sumNumbers(TreeNode(0, TreeNode(1)))