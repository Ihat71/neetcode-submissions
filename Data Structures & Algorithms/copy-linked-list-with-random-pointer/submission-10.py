# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         dummy = Node(0)
#         start = dummy
#         curr = head

#         node_dict = {None: None}

#         while curr:
#             new_node = Node(curr.val)
#             start.next = new_node
#             start = start.next

#             node_dict[curr] = new_node
#             curr = curr.next
        

#         while head:
#             node_dict[head].random = node_dict[head.random] 

#             head = head.next

#         return dummy.next

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        cur = head
        while cur:
            new = Node(cur.val)
            new.next = cur.next
            cur.next = new
            cur = new.next
        
        new = head.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        while cur:
            copy = cur.next
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            cur = cur.next
        
        return new

