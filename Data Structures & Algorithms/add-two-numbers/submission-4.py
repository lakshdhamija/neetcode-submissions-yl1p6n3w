# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, carry = ListNode(), False
        curr = dummy
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sm = num1 + num2
            if carry: sm += 1
            curr.next = ListNode(sm % 10)
            if sm > 9: carry = True
            else: carry = False
            l1, l2, curr = l1.next if l1 else None, l2.next if l2 else None, curr.next
        return dummy.next
