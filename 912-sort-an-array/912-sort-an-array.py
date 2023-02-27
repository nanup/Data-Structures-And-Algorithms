class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    if len(nums) > 1:
      mid = len(nums) // 2
      
      rightArr = nums[mid:]
      leftArr = nums[:mid]
      
      Solution.sortArray(self, leftArr)
      Solution.sortArray(self, rightArr)
      
      i = j = k = 0
      
      while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] > rightArr[j]:
          nums[k] = rightArr[j]
          j += 1
        else:
          nums[k] = leftArr[i]
          i += 1
        k += 1
        
      while i < len(leftArr):
        nums[k] = leftArr[i]
        i += 1
        k += 1
        
      while j < len(rightArr):
        nums[k] = rightArr[j]
        j += 1
        k += 1
        
    return nums