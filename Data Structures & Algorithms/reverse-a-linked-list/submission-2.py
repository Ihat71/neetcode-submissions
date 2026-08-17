# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        previous_node = None
        while True: 
            if head.next:
                next_address = head.next
                head.next = previous_node
                previous_node = head
                head = next_address
            else:
                head.next = previous_node
                break


        return head