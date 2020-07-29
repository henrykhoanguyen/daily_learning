# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False

        cur = head
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        while cur and prev:
            if cur.val != prev.val:
                return False
            else:
                cur = cur.next
                prev = prev.next
        return True

sol = Solution()
print(sol.isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1))))))
print(sol.isPalindrome(ListNode(1,ListNode(2))))
print(sol.isPalindrome(ListNode(1,ListNode(2,ListNode(3,ListNode(2,ListNode(1)))))))
print(sol.isPalindrome(ListNode(0,ListNode(0))))
print(sol.isPalindrome(ListNode(1, ListNode(1, ListNode(2, ListNode(1))))))