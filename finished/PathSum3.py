'''
Problem: 437. Path Sum III
Input: TreeNode - a binary tree; sum - a targeted sum
Output: Number of sub trees that sum up to targeted sum
Explanation:
    We traverse through tree using dfs algorithm and
    subtract node value from sum until we find a node
    with value equal to sum. Once we find a node with
    value equal to sum, we increment count with 1.
    Since there are also a few subtrees in given tree
    that can be sum up to equal targeted sum, we have
    2 functions that help traverse given tree. One
    function that include root value in sum and one
    function that exclude root value. This way the
    latter function would help us find all subtrees
    that would sum up to targeted sum. Run time for
    this problem is O(n log n) ~ O(n^2).
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        self.count = 0

        self.pathSumNoRoot(root, sum)

        return self.count

    def pathSumRoot(self, node, sum):
        if not node:
            return
        if node.val == sum:
            self.count += 1

        self.pathSumRoot(node.left, sum - node.val)
        self.pathSumRoot(node.right, sum - node.val)

    def pathSumNoRoot(self, node, sum):
        if not node:
            return

        self.pathSumNoRoot(node.left, sum)
        self.pathSumNoRoot(node.right, sum)
        self.pathSumRoot(node, sum)
    # def dfs(self, node, sum, total):
    #     if not node:
    #         return
    #
    #     if total >= sum:
    #         if total == sum:
    #             self.count += 1
    #
    #         if node.left:
    #             self.dfs(node.left, sum, node.left.val)
    #         if node.right:
    #             self.dfs(node.right, sum, node.right.val)
    #
    #     elif total < sum:
    #
    #         if node.left:
    #             self.dfs(node.left, sum, total + node.left.val)
    #         if node.right:
    #             self.dfs(node.right, sum, total + node.right.val)


sol = Solution()
sol.pathSum(TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11))), 8)