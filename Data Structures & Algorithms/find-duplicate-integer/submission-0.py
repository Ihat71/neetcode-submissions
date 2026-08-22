class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sets = set()

        for num in nums:
            if num not in sets:
                sets.add(num)
            else:
                return num
        