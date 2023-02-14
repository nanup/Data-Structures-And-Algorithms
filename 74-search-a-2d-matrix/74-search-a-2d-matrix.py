class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    
    left, right = 0, cols - 1
    row = 0
    
    while left <= right and row < rows:
      mid = (left + right) // 2
      
      if target == matrix[row][mid]:
        return True
      elif target > matrix[row][mid]:
        if target > matrix[row][cols - 1]:
          row += 1
        else:
          left = mid + 1
      else:
        right = mid - 1
    
    return False