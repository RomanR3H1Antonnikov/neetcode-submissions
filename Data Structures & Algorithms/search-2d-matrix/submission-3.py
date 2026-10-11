class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1
        while L <= R:
            mid_row = (L + R) // 2
            if matrix[mid_row][0] < target > matrix[mid_row][-1]:
                L = mid_row + 1
            elif matrix[mid_row][0] > target < matrix[mid_row][-1]:
                R = mid_row - 1
            else:
                L, R = 0, len(matrix[mid_row]) - 1
                while L <= R:
                    mid = (L + R) // 2
                    print(mid)
                    print(L, R)
                    if matrix[mid_row][mid] < target:
                        L = mid + 1
                    elif matrix[mid_row][mid] > target:
                        R = mid - 1
                    else:
                        return True
        return False