class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        max_profit = 0
        for _ in range(len(prices) - 1):
            if prices[L] > prices[R]:
                L = R
                R += 1
            else:
                max_profit = max(max_profit, prices[R] - prices[L])
                R += 1
        return max_profit