# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, dummy = head, ListNode()
        dummy.next = head
        second, length = dummy, 0
        while first:
            if length >= n: second = second.next
            first = first.next
            length += 1
        second.next = second.next.next
        return dummy.next

