class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        sum = 0
        for num in nums:
            sum += num
            if not num:
                sum = 0
                continue
            longest = max(longest, sum)
        return longest