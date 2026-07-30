class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap.keys():
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        sorted_array = [x for x, count in sorted(hashmap.items(), key=lambda item: item[1],reverse=True)]
        res = sorted_array[:k]
        print(hashmap)
        return res
