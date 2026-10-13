class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        res = nums[len(nums) - 1]
        while L <= R:
            mid = (L + R) // 2
            res = min(nums[mid], res)
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid - 1
        return res