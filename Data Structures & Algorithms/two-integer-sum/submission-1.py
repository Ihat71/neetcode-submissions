class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        solution = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if solution.get(x, 100000) != 100000:
                return [solution[x], i]
        
            solution[nums[i]] = i