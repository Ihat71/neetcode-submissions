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
        dummy = Node(0)
        start = dummy
        curr = head

        node_dict = {None: None}

        while curr:
            new_node = Node(curr.val)
            start.next = new_node
            start = start.next

            node_dict[curr] = new_node
            curr = curr.next
        

        while head:
            node_dict[head].random = node_dict[head.random] 

            head = head.next

        return dummy.next
