# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
    
        start = list1
        while list1:
            # next_node = list1.next
            while list2:
                buffer = list2.next
                if list2.val >= list1.val and list1.next is not None and list2.val <= list1.next.val:
                    list2.next = list1.next
                    list1.next = list2
                elif list2.val >= list1.val and list1.next is None:
                    print(list2.val)
                    list2.next = None
                    list1.next = list2
                else:
                    break
                
                list2 = buffer
            list1 = list1.next


        return start