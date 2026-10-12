class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        while L <= R:
            k = (L + R) // 2
            sum_piles = sum((pile + k - 1) // k for pile in piles)
            if sum_piles <= h:
                R = k - 1
            else:
                L = k + 1
        return L