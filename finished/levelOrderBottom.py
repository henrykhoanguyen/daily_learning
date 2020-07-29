from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = []
        if not root:
            return []

        queue.append(root)

        def bfs(queue):
            if not queue:
                return
            size = len(queue)
            tmp = []
            for i in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
            bfs(queue)

        bfs(queue)
        print(res[::-1])

sol = Solution()
sol.levelOrderBottom(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
sol.levelOrderBottom(TreeNode(3, TreeNode(9, TreeNode(1), None), TreeNode(20, None,TreeNode(7))))