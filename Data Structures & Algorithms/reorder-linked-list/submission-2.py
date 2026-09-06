# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        print("test")
        if not head: return None
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next: fast = fast.next
        # reverse from slow.next to fast
        reversedList = self.reverseLinkedList(slow.next)
        slow.next = None
        dummy = ListNode()
        curr, l1, l2 = dummy, head, reversedList
        while l1 and l2:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
            curr.next = l2
            l2 = l2.next
            curr = curr.next
        if l1: curr.next = l1
        elif l2: curr.next = l2
        # return dummy.next
