# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        left = l1
        right = l2
        while left and right:
            left.val += carry
            res = left.val + right.val
            carry = 1 if res >= 10 else 0
            left.val = res - 10 if res >= 10 else res

            if not left.next and (right.next or carry):
                left.next = ListNode(0, None)
            left = left.next

            if not right.next and left:
                right.next = ListNode(0, None)
            right = right.next

        return l1