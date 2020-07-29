# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Recursive Approach
        if not q and not p:
            print(True)
            return True
        if (not q and p) or (not p and q):
            print(False)
            return False
        if q.val != p.val:
            print(False)
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # BFS Algorithm Approach
        '''
        if not q and not p:
            return True
        if not q or not p:
            return False

        queueQ, queueP = [], []

        queueP.append(p)
        queueQ.append(q)

        while queueQ or queueP:
            nodeQ = queueQ.pop(0)
            nodeP = queueP.pop(0)

            if nodeQ and nodeP:
                if nodeP.val != nodeQ.val:
                    print(False)
                    return False

            if (not nodeQ and nodeP) or (not nodeP and nodeQ):
                print(False)
                return False

            if nodeQ:
                queueQ.append(nodeQ.left)
                queueQ.append(nodeQ.right)
            if nodeP:
                queueP.append(nodeP.left)
                queueP.append(nodeP.right)

        print(True)
        return True
        '''


sol = Solution()
sol.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))
sol.isSameTree(TreeNode(1, TreeNode(2), None), TreeNode(1, None, TreeNode(2)))
sol.isSameTree(TreeNode(1, TreeNode(1), TreeNode(3)), TreeNode(1, TreeNode(3), TreeNode(1)))
sol.isSameTree(TreeNode(1, TreeNode(2)),TreeNode(1, TreeNode(2)))
sol.isSameTree(TreeNode(None), TreeNode(None))
sol.isSameTree(TreeNode(None), TreeNode(1, TreeNode(2), TreeNode(3)))