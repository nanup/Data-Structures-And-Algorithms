class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix[0]) - 1
        row = 0
        while row < len(matrix):
            if matrix[row][left] <= target <= matrix[row][right]:
                break
            else:
                row += 1
        if row >= len(matrix):
            return False
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right -= 1
            else:
                left += 1
        return False