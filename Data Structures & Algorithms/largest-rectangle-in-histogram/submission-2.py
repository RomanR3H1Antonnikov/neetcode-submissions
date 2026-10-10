class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(len(heights)):
            while stack and stack[-1][1] > heights[i]:
                _, h = stack.pop()
                left_end = 0 if not stack else stack[-1][0] + 1
                width = i - left_end
                area = h * width
                max_area = max(area, max_area)
            stack.append((i, heights[i]))
        while stack:
            _, h = stack.pop()
            left_end = 0 if not stack else stack[-1][0] + 1
            width = len(heights) - left_end
            area = h * width
            max_area = max(area, max_area)
        return max_area