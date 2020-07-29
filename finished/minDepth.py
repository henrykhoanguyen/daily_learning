# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = [[root, 1]]
        res = 999999999999
        while queue:
            node = queue.pop(0)

            if node[0].left == None and node[0].right == None:
                res = min(res, node[1])
            if node[0].left:
                queue.append([node[0].left, node[1] + 1])
            if node[0].right:
                queue.append([node[0].right, node[1] + 1])
        print(res)


sol = Solution()
sol.minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))