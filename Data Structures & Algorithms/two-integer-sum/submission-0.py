class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        n = target

        while i < j:
            if nums[i] + nums[j] == n:
                return [i, j]
            j -= 1
            if i == j:
                j = len(nums)-1
                i += 1 
                 




  
          