class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = 0
        max_length = 0

        for end in range(len(nums)):
            if nums[end] == 1:
                if nums[start] == 0:
                    start = end
                max_length = max(max_length, end - start + 1)
            else:
                start = end

        return max_length
