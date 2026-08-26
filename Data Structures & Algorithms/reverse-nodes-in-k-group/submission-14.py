# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #I want to restart this problem rq

        dummy = ListNode(-1, None)
        tail = dummy
        new_tail = None

        count=0
        while head:
            count+=1
            new_node = head.next
            if not tail.next:
                new_tail = head
            if count == k:
                self.reverseNode(tail, head)
                count = 0
                tail = new_tail
                tmp = new_node
                break_bool = False
                for _ in range(k-1):
                    if not tmp or not tmp.next:
                        tail.next = new_node
                        break_bool = True
                        break
                    tmp = tmp.next
                if break_bool:
                    break
            elif count < k:
                self.reverseNode(tail, head)
            
            head = new_node

        return dummy.next
    def reverseNode(self, tail, head):
        if not tail.next:
            tail.next = head
            tmp = head.next
            head.next = None
                    
        else:
            head.next = tail.next
            tail.next = head
            
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

#         dummy = ListNode(-1)
#         group_prev = dummy
#         curr = head

#         while curr:

#             group_end = curr
#             for _ in range(k):
#                 if not group_end:
#                     return dummy.next
#                 group_end = group_end.next

#             prev = group_end
#             node = curr

#             for _ in range(k):
#                 next_node = node.next
#                 node.next = prev
#                 prev = node
#                 node = next_node

#             group_prev.next = prev

#             group_prev = curr
#             curr = group_end

#         return dummy.next