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
        if not p2:
            return p1
        if not p1:
            return p2

        dummy = ListNode(-1, None)
        dummy.next = p1
        curr = p1
        while curr and p2:
            next_node = p2.next
            if p2.val < curr.val:
                dummy.next = p2
                p2.next = curr
                p2 = next_node
                curr = dummy.next
                continue
            elif curr.next and curr.val <= p2.val <= curr.next.val:
                temp = curr.next
                curr.next = p2
                p2.next = temp
                p2 = next_node
            elif not curr.next and p2.val >= curr.val:
                curr.next = p2
                break
            
            curr = curr.next

        return dummy.next
        