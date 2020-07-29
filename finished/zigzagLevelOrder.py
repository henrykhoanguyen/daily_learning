from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        front = []
        res = []
        front.append([root, 0])
        lvl = 0

        while front:
            tmp = []

            if front[0][1] == front[-1][1]:
                while front and lvl == front[0][1]:
                    node, nodeLevel = front.pop(0)

                    tmp.append(node.val)

                    if node.right:
                        front.append([node.right, nodeLevel + 1])
                    if node.left:
                        front.append([node.left, nodeLevel + 1])

            if lvl % 2 == 0:
                tmp.reverse()
                res.append(tmp)
            else:
                res.append(tmp)

            lvl += 1

        print(res)


sol = Solution()
sol.zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
sol.zigzagLevelOrder(TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7))))
sol.zigzagLevelOrder(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5))))
sol.zigzagLevelOrder(TreeNode(0, TreeNode(2, TreeNode(1, TreeNode(5), TreeNode(1))), TreeNode(4, TreeNode(3, None, TreeNode(6)), TreeNode(-1, None, TreeNode(8)))))