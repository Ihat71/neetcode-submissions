class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                intersection = slow
                break
        slow = nums[0]
        while True:
            if slow == intersection:
                return intersection

            slow = nums[slow]
            intersection = nums[intersection]



        