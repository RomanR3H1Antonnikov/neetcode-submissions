class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        curr_max_len = 1
        for i in nums_set:
            if i - 1 in nums_set and i + 1 not in nums_set:
                continue
            if i - 1 not in nums_set and i + 1 in nums_set:
                curr_len = 1
                while i + curr_len in nums_set:
                    curr_len += 1
                if curr_max_len < curr_len:
                    curr_max_len = curr_len
        return curr_max_len if nums_set else 0