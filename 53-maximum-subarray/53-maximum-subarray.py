class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = -math.inf, 0
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        return maxSum