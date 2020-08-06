'''
Problem: 445. Add Two Numbers II
Input: l1: linked list 1; l2: linked list 2
Output: result linked list
Explanation:
    Using stack1 and stack2, we add linkedList1 and linkedList 2
    into them respectively. while two stacks still have values,
    we add them together from poping at the end of the stack.
    And using carry variable to handle any left over from addition.
    Add result to new linked list and return that linked list.
    Run time complexity is O(n+m) and space complexity is O(n).
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return ListNode()
        carry = 0

        s1 = []
        s2 = []
        s3 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        res = curr = ListNode(0)

        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()

            s3.append(carry % 10)
            carry //= 10

        while s3:
            curr.next = ListNode(s3.pop())
            curr = curr.next

        print(res.next)
        return res.next

sol = Solution()
sol.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
sol.addTwoNumbers(ListNode(9), ListNode(9))
sol.addTwoNumbers(ListNode(7, ListNode(2, ListNode(4, ListNode(3)))), ListNode(5, ListNode(6, ListNode(4))))