class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        pre = 1
        suff = 1
        out = [1] * len_nums

        for i, num in enumerate(nums):
            out[i] *= pre
            pre *= num

        for i, num in enumerate(nums[::-1]):
            j = len_nums - i - 1
            out[j] *= suff
            suff *= num

        return out