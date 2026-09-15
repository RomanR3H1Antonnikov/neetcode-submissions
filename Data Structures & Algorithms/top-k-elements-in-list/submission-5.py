class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in dict1.items():
            bucket[value - 1].append(key)
        ans = []
        for sps in range(len(bucket) - 1, -1, -1):
            if not bucket[sps]:
                continue
            if len(bucket[sps]) >= (k - len(ans)):
                  ans.extend(bucket[sps][:k - len(ans)])
                  return ans
            ans.extend(bucket[sps][:k - len(ans)])