# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        length = 1
        while curr:
            length+=1
            curr = curr.next

        delete_pos = length - n

        curr = ListNode(None, head)
        start = curr
        count = 0
        while curr:
            next_pos = curr.next
            if count == delete_pos-1 and next_pos:
                curr.next = next_pos.next
            elif count == delete_pos:
                curr = None
            count+=1
            curr = next_pos

        return start.next