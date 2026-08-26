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

        curr = head
        count=0

        while curr:
            count+=1
            new_node = curr.next
            if not tail.next:
                new_tail = curr
            if count == k:
                self.reverseNode(tail, curr)
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
                self.reverseNode(tail, curr)
            
            curr = new_node
        return dummy.next
    def reverseNode(self, tail, curr):
        if not tail.next:
            tail.next = curr
            tmp = curr.next
            curr.next = None
                    
        else:
            curr.next = tail.next
            tail.next = curr
            