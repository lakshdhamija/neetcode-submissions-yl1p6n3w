# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, carry = ListNode(), False
        curr = dummy
        while l1 and l2:
            sm = l1.val + l2.val
            if carry: sm += 1
            curr.next = ListNode(sm % 10)
            if sm > 9: carry = True
            else: carry = False
            l1, l2, curr = l1.next, l2.next, curr.next
        while l1:
            sm = l1.val
            # print("before", sm, carry, sm + 1)
            if carry: sm += 1
            # print(sm, carry)
            curr.next = ListNode(sm % 10)
            if sm > 9: carry = True
            else: carry = False
            l1, curr = l1.next, curr.next
        while l2:
            sm = l2.val
            if carry: sm += 1
            curr.next = ListNode(sm % 10)
            if sm > 9: carry = True
            else: carry = False
            l2, curr = l2.next, curr.next
        if carry: curr.next = ListNode(1)
        return dummy.next
