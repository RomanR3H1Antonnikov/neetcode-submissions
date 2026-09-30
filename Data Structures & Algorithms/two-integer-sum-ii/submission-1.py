class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        L, R = 0, len(numbers) - 1
        while numbers[L] + numbers[R] != target:
            if numbers[L] + numbers[R] < target:
                L += 1
                continue
            R -= 1
        ans.append(L + 1)
        ans.append(R + 1)
        return ans