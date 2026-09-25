class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        raw_sets, col_sets, square_sets = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for raw in range(9):
            for col in range(9):
                val = board[raw][col]
                if val == ".":
                    continue
                square_index = (raw // 3) * 3 + (col // 3)
                if val in raw_sets[raw] or val in col_sets[col] or val in square_sets[square_index]:
                    return False
                raw_sets[raw].add(val), col_sets[col].add(val), square_sets[square_index].add(val)
        return True