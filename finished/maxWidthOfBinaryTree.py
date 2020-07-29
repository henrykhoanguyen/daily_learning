# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        queue = [[root, 1, 1]]

        while queue:
            if len(queue) > 1 and queue[0][2] == queue[-1][2]:
                res = max(queue[-1][1] - queue[0][1] + 1, res)

            node = queue.pop(0)
            # print(node[0].val, node[1], node[2])
            if node[0].left:
                queue.append([node[0].left, node[1] * 2, node[2] + 1])
            if node[0].right:
                queue.append([node[0].right, node[1] * 2 + 1, node[2] + 1])

        print(res)


sol = Solution()
sol.widthOfBinaryTree(TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9))))
sol.widthOfBinaryTree(TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), None))
sol.widthOfBinaryTree(TreeNode(1, TreeNode(3, TreeNode(5), None), TreeNode(2)))
sol.widthOfBinaryTree(TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, None, TreeNode(7)))))
