class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        output = []

        for i, num in enumerate(nums):
            target = -1 * num
            answer = [num]
            j = 0
            k = len(nums) - 1
            while(j < k):
                if nums[j] + nums[k] > target or k == i:
                    k-=1
                elif nums[j] + nums[k] < target or j == i:
                    j += 1
                elif nums[j] + nums[k] == target:
                    answer.append(nums[j])
                    answer.append(nums[k])
                    if sorted(answer) not in output:
                        output.append(sorted(answer))
                        print(nums[i], nums[j], nums[k], i, j, k)
                    answer=[num]
                    j += 1
                    k -= 1


        return output