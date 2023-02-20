class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #each row is sorted in ascending order
    #the first integer of each row is greater than the last integer of the previous row
    
    #o(log(m * n))
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    first, last = 0, rows * cols - 1
    
    while first <= last :
      mid = (first + last) // 2
      
      row = mid // cols
      col = mid % cols
      
      num = matrix[row][col]
      
      if num == target:
        return True
      elif num < target:
        first = mid + 1
      else:
        last = mid - 1
        
    return False