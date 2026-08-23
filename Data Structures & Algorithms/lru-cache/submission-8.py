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
    def __init__(self, key: int, val: int, next_node=None, before=None):
        self.key = key
        self.val = val
        self.next = next_node
        self.before = before


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # Dummy head.
        # head.next is always the LRU node.
        self.head = Node(-1, -1)

        # Tail / MRU node
        self.linked = None

        # key -> Node
        self.seen = {}

        self.count = 0

    def get(self, key: int) -> int:
        if key not in self.seen:
            return -1

        node = self.seen[key]

        # Accessing a node makes it MRU
        self.switch_first(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.seen:
            node = self.seen[key]
            node.val = value

            # Updating a key also makes it MRU
            self.switch_first(node)
            return

        # Cache is full -> remove LRU
        if self.count == self.capacity:
            lru = self.head.next

            # Remove from dictionary
            del self.seen[lru.key]

            # Move head past LRU
            self.head.next = lru.next

            if lru.next:
                lru.next.before = None
            else:
                # Cache had only one node
                self.linked = None

            self.count -= 1

        # Add new node as MRU
        node = Node(key, value)

        if self.linked is None:
            # First node
            self.head.next = node
            self.linked = node

        else:
            # Add after current MRU
            self.linked.next = node
            node.before = self.linked
            self.linked = node

        self.seen[key] = node
        self.count += 1

    def switch_first(self, node):
        # Already MRU
        if node == self.linked:
            return

        before = node.before
        after = node.next

        # Remove node from its current position
        if before:
            before.next = after
        else:
            # node was LRU
            self.head.next = after

        if after:
            after.before = before

        # Put node at MRU
        node.before = self.linked
        node.next = None

        self.linked.next = node
        self.linked = node



