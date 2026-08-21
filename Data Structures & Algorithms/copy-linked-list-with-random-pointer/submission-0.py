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
        dummy = Node(0, None, None)
        start = dummy
        curr = head

        node_dict = dict()

        while curr and start:
            new_node = Node(curr.val, None, None)
            start.next = new_node
            start = start.next

            node_dict[curr] = new_node
            curr = curr.next
        
        curr = head
        start = dummy.next

        while curr and start:
            start.random = node_dict[curr.random] if curr.random else None

            start = start.next
            curr = curr.next

        return dummy.next
