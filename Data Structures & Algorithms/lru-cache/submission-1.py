class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pouch = dict()
        self.count = 0
    def get(self, key: int) -> int:
        if key in self.pouch:
            self.count += 1
            old_val = self.pouch[key]
            new_val = [self.count, old_val[1]]
            self.pouch[key] = new_val
            return self.pouch[key][1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.count+=1
        if key not in self.pouch and len(self.pouch) >= self.capacity:
            minimum = min([x[0] for x in self.pouch.values()])
            for k, v in self.pouch.items():
                if v[0] == minimum:
                    self.pouch.pop(k)
                    break
            self.pouch[key] = [self.count, value]

        else:
            self.pouch[key] = [self.count, value]
