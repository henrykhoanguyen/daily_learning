# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0
        tmp = head
        res = 0
        while tmp != None:
            count += 1
            tmp = tmp.next

        while head != None:
            count -= 1
            if head.val == 1:
                res += 2**(count)
            head = head.next

        print(res)

sol = Solution()
sol.getDecimalValue(ListNode(1,ListNode(0,ListNode(1))))
sol.getDecimalValue(ListNode(1))
sol.getDecimalValue(ListNode(0))
sol.getDecimalValue(ListNode(1, ListNode(0, ListNode(0, ListNode(1, ListNode(0, ListNode(0, ListNode(1, ListNode(1, ListNode(1, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0))))))))))))))))