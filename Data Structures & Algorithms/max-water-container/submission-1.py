class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        max_square = 0
        while L < R:
            min_height = min(heights[L], heights[R])
            square = (R - L) * min_height
            if max_square < square:
                max_square = square
                continue
            if min_height == heights[L]:
                L += 1
                continue
            R -= 1
        return max_square