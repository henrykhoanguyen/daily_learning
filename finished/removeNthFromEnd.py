# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        length = 0
        stack = []
        temp = head

        while temp != None:
            stack.append(temp)
            temp = temp.next

        temp = stack[0]
        if n > len(stack):
            self.printList(temp)
            return temp

        if n == len(stack):
            temp = temp.next
            stack[0].next = None
            self.printList(temp)
            return temp

        if stack[len(stack) - n]:
            stack[len(stack) - n - 1].next = stack[len(stack) - n].next

        self.printList(head)


    def printList(self, head: ListNode):
        while head != None:
            print(head.val)
            head = head.next
        print()

sol = Solution()
sol.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))), 2)
sol.removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))), 5)
sol.removeNthFromEnd(ListNode(1), 1)
sol.removeNthFromEnd(ListNode(), 1)
sol.removeNthFromEnd(ListNode(1, ListNode(2)), 4)