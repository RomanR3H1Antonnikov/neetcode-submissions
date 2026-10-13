class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        res = nums[len(nums) - 1]
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                res = min(nums[mid], res)
                L = mid + 1
            else:
                res = min(nums[mid], res)
                R = mid - 1
        return res