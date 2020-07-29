# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        curr = ListNode(-1)
        curr.next = head
        tmp = curr

        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next

        tmp = tmp.next
        while tmp:
            print(tmp.val)
            tmp = tmp.next
        print()

sol = Solution()
sol.removeElements(ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), 6)
sol.removeElements(ListNode(6, ListNode(6, ListNode(6, ListNode(6, ListNode(4, ListNode(5, ListNode(6))))))), 6)
sol.removeElements(ListNode(1, ListNode(2, ListNode(6, ListNode(6, ListNode(6, ListNode(5, ListNode(6))))))), 6)

