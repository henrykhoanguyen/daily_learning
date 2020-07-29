
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False


        def isSubHelper(s, t):
            if s is None or t is None:
                return s is None and t is None

            if s.val == t.val:
               return isSubHelper(s.left, t.left) and isSubHelper(s.right, t.right)
            else:
                return False

        if isSubHelper(s, t):
            return True
        elif self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True

        return False

sol = Solution()
print(sol.isSubtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)), TreeNode(4, TreeNode(1), TreeNode(2))))