class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        anslist = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
                continue
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix_product = 1
            else:
                suffix_product = suffix_product * nums[i + 1]
            anslist[i] = prefix[i] * suffix_product
        return anslist
