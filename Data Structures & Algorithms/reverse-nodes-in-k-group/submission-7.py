# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1, None)

        tail = dummy
        new_tail = None
        curr = head
        if k == 1:
            return curr

        length = 0
        while curr:
            curr = curr.next
            length += 1 

        edge = False
        if (length) % k != 0:
            edge = True

        valid_pos = length - (length % k)


        count = 1
        curr = head
        while curr:
            new_node = curr.next
            if edge and count > valid_pos:
                tail.next = curr
                break
            if not tail.next:
                curr.next = None
                tail.next = curr
                new_tail = curr
            elif count % k == 0:
                temp = tail.next
                tail.next = curr
                curr.next = temp
                tail = new_tail
            elif count % k != 0:
                temp = tail.next
                tail.next = curr
                curr.next = temp


            count+=1
            curr = new_node


        return dummy.next