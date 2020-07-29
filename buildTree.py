from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or postorder:
            return TreeNode()



sol = Solution()
sol.buildTree([9,3,15,20,7], [9,15,7,20,3])