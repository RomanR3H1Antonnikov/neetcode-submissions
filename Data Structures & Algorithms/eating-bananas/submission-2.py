class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 999999999999
        L, R = 1, max(piles)
        while L <= R:
            mid = k = (L + R) // 2
            sum_piles = sum((pile + k - 1) // k for pile in piles)
            if sum_piles <= h:
                res = min(k, res)
                R = mid - 1
            else:
                L = mid + 1
        return res
