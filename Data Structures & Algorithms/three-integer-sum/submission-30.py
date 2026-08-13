class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        seen = set()

        for i, num in enumerate(nums):
            target = -1 * num
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                if nums[j] + nums[k] > target:
                    k-=1
                elif nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] == target:
                    answer = (nums[i], nums[j], nums[k])
                    #if you can prevent lookup this can get to sub 150 ms potentially
                    if answer not in seen:
                        seen.add(answer)
                        output.append(answer)
                    j += 1
                    k -= 1


        return output

