class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        start, end = 0, 0
        max_freq = 0
        num_sum = 0

        for end in range(len(nums)):
            num_sum += nums[end]

            while (end-start+1) * nums[end] - num_sum> k:
                num_sum -= nums[start]
                start += 1

            max_freq = max(max_freq, (end-start+1))

        return max_freq
