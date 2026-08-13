# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums = sorted(nums)
#         output = []
#         seen = set()

#         for i, num in enumerate(nums):
#             target = -1 * num
#             j = i + 1
#             k = len(nums) - 1
#             while(j < k):
#                 if nums[j] + nums[k] > target:
#                     k-=1
#                 elif nums[j] + nums[k] < target:
#                     j += 1
#                 elif nums[j] + nums[k] == target:
#                     answer = (nums[i], nums[j], nums[k])
#                     #if you can prevent O(n) lookup this can get to sub 150 ms potentially
#                     if answer not in seen:
#                         seen.add(answer)
#                         output.append(answer)
#                     j += 1
#                     k -= 1


#         return output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            # Skip duplicate first values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since array is sorted, no three numbers can sum to 0
            # once the first number is positive.
            if nums[i] > 0:
                break

            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:
                total = nums[j] + nums[k]

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    output.append([nums[i], nums[j], nums[k]])

                    # Skip duplicate second values
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    # Skip duplicate third values
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

        return output