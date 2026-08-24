# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.pouch = dict()
#         self.count = 0
#     def get(self, key: int) -> int:
#         if key in self.pouch:
#             self.count += 1
#             old_val = self.pouch[key]
#             new_val = [self.count, old_val[1]]
#             self.pouch[key] = new_val
#             return self.pouch[key][1]
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         self.count+=1
#         if key not in self.pouch and len(self.pouch) >= self.capacity:
#             minimum = min([x[0] for x in self.pouch.values()])
#             for k, v in self.pouch.items():
#                 if v[0] == minimum:
#                     self.pouch.pop(k)
#                     break
#             self.pouch[key] = [self.count, value]

#         else:
#             self.pouch[key] = [self.count, value]

class Node:
    def __init__(self, key: int , val: int, next_node = None, before = None):
        self.key = key
        self.val = val
        self.next = next_node
        self.before = before

    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked = None
        self.head = Node(-1, -1)
        self.seen = dict()

    def get(self, key: int) -> int:
        if key in self.seen:
            self.switch_head(self.seen[key])
            return self.seen[key].val
        
        return -1


    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)

        if key in self.seen:
            curr = self.seen[key]
            curr.val = value
            self.switch_head(curr)
            return

        elif not self.linked:
            self.head.next = new_node

        elif self.linked and len(self.seen) < self.capacity:
            new_node.before = self.linked
            self.linked.next = new_node
        
        elif self.linked and len(self.seen) == self.capacity:
            lfu = self.head.next
            next_lfu = lfu.next
            if next_lfu:
                self.head.next = next_lfu
                next_lfu.before = None
            self.seen.pop(lfu.key)
            lfu = None
            new_node.before = self.linked
            self.linked.next = new_node
            
        
        self.linked = new_node
        self.seen[key] = self.linked
        
            
    def switch_head(self, node):
        if node == self.linked:
            return

        before = node.before
        after = node.next

        if before:
            before.next = after
        else:
            self.head.next = after

        if after:
            after.before = before

        node.before = self.linked
        node.next = None
        self.linked.next = node
        self.linked = node



