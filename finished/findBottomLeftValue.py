# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = [root]
        res = 0

        while queue:
            if len(queue) == 1:
                res = queue[0].val

            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        print(res)


sol = Solution()
sol.findBottomLeftValue(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
sol.findBottomLeftValue(TreeNode(2, TreeNode(1), TreeNode(3)))
sol.findBottomLeftValue(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6))))