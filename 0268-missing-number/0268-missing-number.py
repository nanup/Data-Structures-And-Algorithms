class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1 = xor2 = 0

        for i in range(len(nums)):
          xor1 ^= nums[i]
          xor2 ^= i

        xor2 ^= len(nums)

        return xor1 ^ xor2