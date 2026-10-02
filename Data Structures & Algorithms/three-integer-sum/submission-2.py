class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i != 0:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                if nums[L] + nums[R] + nums[i] < 0:
                    L += 1
                    continue
                elif nums[L] + nums[R] + nums[i] > 0:
                    R -= 1
                    continue
                result.append([nums[i], nums[L], nums[R]])
                L += 1
                while L < R and nums[L] == nums[L - 1]:
                    L += 1
        return result