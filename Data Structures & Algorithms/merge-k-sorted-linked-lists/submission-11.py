# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         dummy = ListNode(-1, None)
        # for node in lists:
        #     if not node:
        #         continue
        #     if not dummy.next:
        #         dummy.next = node
        #     else:
        #         start = dummy.next
        #         curr = node
        #         while start and curr:
        #             if start.next and start.val < curr.val <= start.next.val:
        #                 next_node = curr.next
        #                 curr.next = start.next
        #                 start.next = curr
        #                 curr = next_node
        #             elif curr.val <= start.val:
        #                 next_node = curr.next
        #                 dummy.next = curr
        #                 curr.next = start
        #                 curr = next_node
        #                 start = dummy.next
        #                 continue
        #             elif not start.next and curr.val >= start.val:
        #                 start.next = curr
        #                 break
        #             start = start.next           

        # return dummy.next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            new_list = []
            len_list = len(lists)

            for i in range(0, len_list, 2):
                p1 = lists[i]
                p2 = lists[i+1] if i+1 < len_list else None

                new_list.append(self.mergeLists(p1, p2))
            
            lists = new_list
            
    

        return lists[0]

        
    def mergeLists(self, p1, p2):

        dummy = ListNode(-1, None)
        tail = dummy
        
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
        
            tail = tail.next

        if p1:
            tail.next = p1
        if p2:
            tail.next = p2

        return dummy.next
        