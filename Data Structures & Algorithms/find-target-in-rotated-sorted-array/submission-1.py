class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l<=r:

            mid = (r + l) // 2
            # print(l, r, mid)

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            elif nums[mid] <= nums[r]:
                if nums[r] >= target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
 

            
        return -1

        