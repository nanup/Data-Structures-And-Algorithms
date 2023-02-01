class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        
        def recurse(i, currSum, maxSum):
            if i == len(nums):
                return maxSum
            
            if nums[i] > nums[i] + currSum:
                currSum = nums[i]
                maxSum = max(maxSum, nums[i])
            else:
                currSum += nums[i]
                maxSum = max(maxSum, currSum)
                
            return recurse(i + 1, currSum, maxSum)
            
        maxSum = recurse(1, currSum, maxSum)
        return maxSum