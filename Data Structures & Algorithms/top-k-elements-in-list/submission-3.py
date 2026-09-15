class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            if num in dict1:
                dict1[num] += 1
                continue
            dict1[num] = 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in dict1.items():
            bucket[value - 1].append(key)
        ans = []
        for sps in range(len(bucket) - 1, -1, -1):
            if not bucket[sps]:
                continue
            if len(bucket[sps]) >= (k - len(ans)):
                  ans.extend(bucket[sps][:k])
                  return ans
            ans.extend(bucket[sps][:k])