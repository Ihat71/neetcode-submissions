# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        middle = slow
        while True:
            next_pos = slow.next
            slow.next = prev
            prev = slow
            if next_pos == None:
                break
            slow = next_pos
        
        tail = slow
        curr = head
        while curr and tail and tail.next:
            if curr == middle:
                break
            next_curr, next_tail = curr.next, tail.next
            tail.next = curr.next
            curr.next = tail

            tail = next_tail
            curr = next_curr

