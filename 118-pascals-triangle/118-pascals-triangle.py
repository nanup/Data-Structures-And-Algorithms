class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for i in range(1, numRows + 1):
          rowResult = [1] * i
          
          for j in range(1, i - 1):
            rowResult[j] = result[-1][j] + result[-1][j - 1]
            
          result.append(rowResult)
          
        return result