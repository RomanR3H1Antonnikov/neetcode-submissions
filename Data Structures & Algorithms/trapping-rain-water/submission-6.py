class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        max_L, max_R = height[0], height[-1]
        L, R = 0, len(height) - 1
        ans_amount = 0
        while L < R:
            if max_L > max_R:
                R -= 1
                max_R = max(max_R, height[R])
                ans_amount += max_R - height[R]
            else:
                L += 1
                max_L = max(max_L, height[L])
                ans_amount += max_L - height[L]
        return ans_amount