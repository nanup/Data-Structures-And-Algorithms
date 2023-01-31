class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        currSum = 0
        
        pointer = 0
        
        while pointer < len(nums):
            currSum += nums[pointer]
            
            if currSum < 0:
                currSum = 0
            
            maxSum = max(maxSum, currSum)
            
            pointer += 1
            
        if not maxSum:
            return max(nums)
        
        return maxSum