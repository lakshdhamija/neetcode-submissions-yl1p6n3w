# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        curr, prev, tail = head, None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return (prev, tail)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr, size, groupPrev = head, 0, dummy
        while curr:
            size += 1
            # print("outside", size, curr.val)
            if size % k == 0:
                # print("inside", size, curr.val)
                nxt = curr.next
                curr.next = None
                newHead, newTail = self.reverseList(groupPrev.next)
                groupPrev.next = newHead
                groupPrev = newTail
                newTail.next = nxt
                curr = newTail
            curr = curr.next
        return dummy.next