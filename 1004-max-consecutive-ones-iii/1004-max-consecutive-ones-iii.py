class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        windowStart = 0
        maxLength = 0
        zeroCount = 0
        
        for windowEnd in range(len(nums)):
          digit = nums[windowEnd]
          
          if digit == 0:
            zeroCount += 1
          
          while zeroCount > k:
            newDigit = nums[windowStart]
            
            if newDigit == 0:
              zeroCount -= 1
            
            windowStart += 1 
              
          maxLength = max(maxLength, windowEnd - windowStart + 1)
          
        return maxLength